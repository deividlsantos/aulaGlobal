from rest_framework import viewsets, authentication, permissions
from .serializers import ProductSerializer
from .models import Product


class ProductViewSet(viewsets.ModelViewSet):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = (authentication.TokenAuthentication,)