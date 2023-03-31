from django.conf import settings
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.utils.translation import activate
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.views.generic import ListView
from django.views.static import serve

from ilan.models import Like, Dislike, Ip, Favorite
from ilan.models import Product


class ProductListView(ListView):
    model = Product
    context_object_name = "products"
    template_name = "ilan/index.html"


# chatgpt3
@require_POST
@csrf_exempt
def add_like(request, post_id):
    product = get_object_or_404(Product, id=post_id)
    ip, created = Ip.objects.get_or_create(ip=request.META.get('REMOTE_ADDR'))
    if not product.has_liked(ip):
        like = Like(product=product, ip=ip)
        like.save()
        return JsonResponse({'status': 'ok'})
    else:
        return JsonResponse({'status': 'error', 'message': 'You have already liked this product.'})


@require_POST
@csrf_exempt
def add_dislike(request, post_id):
    product = get_object_or_404(Product, id=post_id)
    ip, created = Ip.objects.get_or_create(ip=request.META.get('REMOTE_ADDR'))
    if not product.has_disliked(ip):
        dislike = Dislike(product=product, ip=ip)
        dislike.save()
        return JsonResponse({'status': 'ok'})
    else:
        return JsonResponse({'status': 'error', 'message': 'You have already disliked this post.'})


@require_POST
@csrf_exempt
def add_favorite(request, post_id):
    product = get_object_or_404(Product, id=post_id)
    ip, created = Ip.objects.get_or_create(ip=request.META.get('REMOTE_ADDR'))
    if not product.has_favorited(ip):
        favorite = Favorite(product=product, ip=ip)
        favorite.save()
        return JsonResponse({'status': 'ok'})
    else:
        return JsonResponse({'status': 'error', 'message': 'You have already favorited this post.'})


def products(request):
    if request.GET.get('type') == 'top':
        products = Product.objects.filter(top_offer=True)
    elif request.GET.get('type') == 'new':
        products = Product.objects.filter(new_offer=True)
    elif request.GET.get('type') == 'hot':
        products = Product.objects.filter(hot_deal=True)
    else:
        products = Product.objects.all()

    data = {
        'products': list(products.values())
    }
    return JsonResponse(data)


# Ваша функция-контроллер здесь
def serve_video(request):
    response = serve(request, 'video/main.mp4', document_root=settings.STATIC_ROOT)
    response['Cache-Control'] = 'max-age=86400'  # кэшировать


def set_language(request):
    if request.method == 'POST':
        language_code = request.POST.get('language')
        if language_code:
            activate(language_code)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
