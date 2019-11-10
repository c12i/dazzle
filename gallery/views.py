from django.shortcuts import render
from gallery.models import Photo

# Create your views here.
def index(request):
    photos = Photo.show_all_photos()
    return render(request, "gallery/index.html", context={"photos":photos})

def search(request):
    
    if request.method == "GET":
        search_term = request.GET.get("search")
        searched_photos = Photo.search_photo_by_category(search_term)
        results = len(searched_photos)
        message = "{}".format(search_term)
        
        return render(request, "gallery/search.html", context={"message":message,
                                                               "photos":searched_photos,
                                                               "results":results})
    else:
        message = "You have not searched for any photo"
        return render(request, "gallery/search.html", context={"message":message})
