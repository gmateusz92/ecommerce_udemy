from .models import Category

def menu_links(request): #do wyswietlania linkow w templates uzywane
    links = Category.objects.all()
    return dict(links=links)