from django.urls import path
from ilan.views import TopProductListView, NewProductListView, HotProductListView
from ilan.views import ProductListView, List
from ilan.views import ProductFilterAPIView

urlpatterns = [
    path('', ProductListView.as_view(), name="home"),
    path('favorite/', List.as_view(), name="favorite"),
    path('top/', TopProductListView.as_view(), name="top_products"),
    path('new/', NewProductListView.as_view(), name="new_products"),
    path('hot/', HotProductListView.as_view(), name="hot_products"),
    path('filter/', ProductFilterAPIView.as_view(), name="filter"),
]
