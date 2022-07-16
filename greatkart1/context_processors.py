from .models import Category

def menu_links(request): #do wyswietlania linkow w all category
    links = Category.objects.all()
    return dict(links=links)