from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
from ilan.models import Product


class RobotsView(TemplateView):
    template_name = 'config_site/robots.txt'
    content_type = 'text/plain'  # this is important! It tells the browser that this is a text file


class SitemapView(TemplateView):
    template_name = 'config_site/sitemap.xml'
    content_type = 'application/xml'  # this is important! It tells the browser that this is a text file

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.all()
