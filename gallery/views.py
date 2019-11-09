from django.shortcuts import render
from gallery.models import Photo

# Create your views here.
def index(request):
    photos = Photo.show_all_photos()
    return render(request, "gallery/index.html", context={"photos":photos})
