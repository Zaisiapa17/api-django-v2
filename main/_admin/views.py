from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from . import serializers
from . import models


@api_view(['GET', 'POST'])
def admin_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        admins = models.Admin.objects.all()
        serializer = serializers.AdminSerializer(admins, many=True)
        data_response = {
            'data': serializer.data,
            'status': "success"
        }
        return Response(data_response)