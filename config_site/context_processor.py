from config_site.models import Title, SubTitle


def get_title(request):
    title = Title.objects.last()
    return dict(title=title)


def get_subtitle(request):
    subtitle = SubTitle.objects.last()
    return dict(subtitle=subtitle)
