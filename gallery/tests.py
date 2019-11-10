from django.test import TestCase
from gallery.models import Photo, Location, Category
import datetime

# Create your tests here.
class PhotoTestClass(TestCase):
    """
    Creating the initial instance of the Photo class
    """
    def setUp(self):
        self.place = Location(city = "Nairobi", country = "Kenya")
        self.place.save()

        self.category = Category(name = "Test")
        self.category.save()

        self.photo = Photo(name = 'A random title', description = "A random description",
                           location = self.place)
        self.photo.save()
    
    def test_instance(self):
        self.assertTrue(isinstance(self.photo, Photo))

    def test_save_method(self):
        self.photo.save_photo()
        photos = Photo.objects.all()
        self.assertTrue(len(photos) > 0)

    def test_delete_method(self):
        Photo.delete_photo(self.photo.id)
        photos = Photo.objects.all()
        self.assertTrue(len(photos) == 0)

    def test_get_photo_by_id(self):
        photo = Photo.get_photo_by_id(self.photo.id)
        self.assertEqual(photo, self.photo)

    def test_search_photo_by_category(self):
        photos = Photo.search_photo_by_category("Test")
        self.assertFalse(len(photos) > 0)

    def test_filter_by_location(self):
        pass


class LocationTestClass(TestCase):
    """
    Testing the Location class
    """
    def setUp(self):
        """
        Creating a new instance of the Location class
        """
        self.place = Location(city = "Nairobi", country = "Kenya")
        self.place.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.place, Location))

    def test_save_method(self):
        places = Location.objects.all()
        self.assertTrue(len(places) > 0)
        

class CategoryTestClass(TestCase):
    """
    Testing the Category class
    """
    def setUp(self):
        """
        Creating a new instance of the Category class
        """
        self.category = Category(name = "Test")
        self.category.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.category, Category))

    def test_save_method(self):
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)

