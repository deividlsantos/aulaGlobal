from rest_framework import serializers
from .models import Product, CategoryProduct


class CategoryProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryProduct
        fields = ('name',)

class ProductSerializer(serializers.ModelSerializer):

    number = serializers.IntegerField(source='id')
    category = CategoryProductSerializer(read_only=True)
    class Meta:
        model = Product
        exclude = ('id',)

    def get_type(self, obj):
        types = dict(Product.TYPE_CHOYCE)
        return types[obj.Poduct]
