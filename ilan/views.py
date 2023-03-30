from django.db.models import Q
from django.views.generic import ListView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from .models import Category, Rooms, Area, Product
from .serializers import ProductSerializer


class ProductListView(ListView):
    model = Product
    context_object_name = "products"
    template_name = "ilan/index.html"


class TopProductListView(ListView):
    model = Product
    context_object_name = "products"
    template_name = "ilan/index.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["products"] = Product.objects.filter(top_offer=True)
        return context


class NewProductListView(ListView):
    model = Product
    context_object_name = "products"
    template_name = "ilan/index.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["products"] = Product.objects.filter(new_offer=True)
        return context


class HotProductListView(ListView):
    model = Product
    context_object_name = "products"
    template_name = "ilan/index.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["products"] = Product.objects.filter(hot_deal=True)
        return context


# API
# ListFilter
class ProductFilterAPIView(ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = Product.objects.all()

        # Фильтр по категориям
        category_id = self.request.GET.get('category')
        if category_id:
            try:
                category = Category.objects.get(pk=category_id)
                queryset = queryset.filter(category=category)
            except Category.DoesNotExist:
                pass

        # Фильтр по комнатам
        rooms_id = self.request.GET.get('room')
        if rooms_id:
            try:
                rooms = Rooms.objects.get(pk=rooms_id)
                queryset = queryset.filter(rooms=rooms)
            except Rooms.DoesNotExist:
                pass

        # Фильтр по географической зоне
        area_id = self.request.GET.get('geo')
        if area_id:
            try:
                area = Area.objects.get(pk=area_id)
                queryset = queryset.filter(area=area)
            except Area.DoesNotExist:
                pass

        # Фильтр по цене
        min_price = self.request.GET.get('min')
        max_price = self.request.GET.get('max')
        if min_price and max_price:
            queryset = queryset.filter(Q(price__gte=min_price) & Q(price__lte=max_price))
        elif min_price:
            queryset = queryset.filter(price__gte=min_price)
        elif max_price:
            queryset = queryset.filter(price__lte=max_price)

        return queryset

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

