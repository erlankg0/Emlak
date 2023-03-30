from home.models import Category, Rooms, Area


def get_all_categories(request):
    categories = Category.objects.all()
    return dict(categories=categories)


def get_all_rooms(request):
    rooms = Rooms.objects.all()
    return dict(rooms=rooms)


def get_all_areas(request):
    areas = Area.objects.all()
    return dict(areas=areas)
