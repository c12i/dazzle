import os
# configure settings for the project
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gallery_project.settings")

import django
django.setup()

#Population Scripts
import random
from gallery.models import Category
from faker import Faker

fake = Faker()

def add_category():
    # get or create returns an object and something that's created, we are interested in the object hence why we index 0
    topics = ["Scenery", "Peaceful", "Animals", "Birds", "Forest", "Snow", 
          "Winter", "Beach", "Autumn", "Miscellaneous", "Farm", "City",
          "Portrait", "Fall", "Desert"]

    for t in topics:
        categ = Category.objects.get_or_create(name = t)[0]
        categ.save()
        
    return categ


if __name__ == "__main__":
    print("populating database...")
    add_category()
    print("Done")