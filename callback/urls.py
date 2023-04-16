from django.urls import path

from .views import CallbackCreateView

urlpatterns = [
    path('create-callback/', CallbackCreateView.as_view(), name='create-callback'),
]
