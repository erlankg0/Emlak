from rest_framework import serializers
from .models import Product, Image, Rooms


class ImageSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()

    class Meta:
        model = Image
        fields = ('url',)

    def get_url(self, obj):
        return obj.image.url


class RoomsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rooms
        fields = ('title',)


class ProductSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)
    rooms = RoomsSerializer(many=True, read_only=True)
    category_title = serializers.CharField(source='category.title')

    class Meta:
        model = Product
        fields = ('id', 'title', 'description', 'price', 'category_title', 'rooms', 'area', 'images')
