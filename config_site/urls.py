from django.urls import path
from config_site.views import SitemapView, RobotsView

urlpatterns = [
    path('sitemap/', SitemapView.as_view(), name="sitemap"),
    path('robots.txt', RobotsView.as_view(), name='robots'),
]
