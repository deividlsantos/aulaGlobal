from rest_framework import viewsets, authentication, permissions
from .serializers import ProviderSerializer
from rest_framework.pagination import PageNumberPagination
from .models import Provider

class MyPageNumberPagination(PageNumberPagination):

    page_size = 2

class ProviderViewSet(viewsets.ModelViewSet):

    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    pagination_class = MyPageNumberPagination