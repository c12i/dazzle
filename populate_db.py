import os
# configure settings for the project
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gallery_project.settings")

import django
django.setup()

#Population Scripts
import random
from gallery.models import Category, Location
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

def populate_locations(N=10):
    for entry in range(N):
        fake_city = fake.city()
        fake_country = fake.country()

        new_location = Location.objects.get_or_create(city = fake_city, 
                                              country = fake_country)[0]
        new_location.save()


if __name__ == "__main__":
    print("populating database...")
    # add_category()
    populate_locations(20)
    print("Done")