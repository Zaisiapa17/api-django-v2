from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

from . import serializers
from . import models


# class CustomPagination(PageNumberPagination):
#     page_size = 10
#     page_size_query_param = 'page_size'
#     max_page_size = 100


@api_view(['GET'])
def products(request):
    products = models.Product.objects.all().order_by('id')
    paginator = PageNumberPagination()
    result_page = paginator.paginate_queryset(products, request)
    serializer = serializers.ProductSerializer(result_page, many=True)
    data_response = {
        'status': "success",
        'count': paginator.page.paginator.count,
        'next': paginator.get_next_link(),
        'previous': paginator.get_previous_link(),
        'data': serializer.data,
    }
    return Response(data_response)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def product_list(request, pk):
    if request.method == 'GET':
        try:
            product = models.Product.objects.get(pk=pk)
            serializer = serializers.ProductSerializer(product)
            data_response = {
                'data': serializer.data,
                'status': "success"
            }
            return Response(data_response)

        except models.Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)