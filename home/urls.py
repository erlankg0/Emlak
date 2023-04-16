from django.urls import path

from home.views import ProductListView, set_language, AboutView
from .views import add_like, add_dislike, add_favorite, products, serve_video

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name="about"),
    path('add_like/<int:post_id>/', add_like, name='add_like'),
    path('add_dislike/<int:post_id>/', add_dislike, name='add_dislike'),
    path('add_favorite/<int:post_id>/', add_favorite, name='add_favorite'),
    path('api/products/', products, name='products'),
    path('video/main.mp4', serve_video, name='serve_video'),

]
