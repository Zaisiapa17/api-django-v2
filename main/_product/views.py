from django.shortcuts import render
from rest_framework import permissions, viewsets
from . import serializers
from . import models

# Create your views here.
class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer
    permission_classes = [permissions.IsAuthenticated]