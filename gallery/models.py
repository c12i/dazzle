from django.db import models

# Create your models here.

class Location(models.Model):
    """
    A class for geographic loactions where a Photo could be taken
    """
    city = models.CharField(max_length=244)
    country = models.CharField(max_length=244)

    def __str__(self):
        """
        String representation
        """
        return self.city

    def save_location(self):
        """
        A method to save the location name
        """
        return self.save()

class Category(models.Model):
    """
    A class for the category the Photo falls under
    """
    name = models.CharField(max_length=144)

    def __str__(self):
        """
        String representation
        """
        return self.name

    def save_category(self):
        """
        A method to save the category name
        """
        return self.save()


class Photo(models.Model):
    """
    A class thaat determines how photos will be saved into the database
    """
    name = models.CharField(max_length=244)
    description = models.TextField()
    location = models.ForeignKey(Location)
    categories = models.ManyToManyField(Category)
    post_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="articles/")

    def __str__(self):
        """
        String representation
        """
        return self.name

    def save_photo(self):
        """
        A method to save the photo
        """
        return self.save()
    
    @classmethod
    def show_all_photos(cls):
        """
        A method to return all photos posted in order of the most recent to oldest
        """
        return cls.objects.order_by("post_date")

    
    @classmethod
    def delete_photo(cls, id):
        """
        A method to delete an object
        """

        return cls.objects.filter(id = id).delete()


    @classmethod
    def get_photo_by_id(cls, id):
        """
        A method to get a photo based on its id
        """
        return cls.objects.filter(id = id)

    @classmethod
    def search_photo_by_category(cls, search):
        """
        A method to return all photos that fall under a certain catergory
        """
        return cls.objects.filter(category = search)

    @classmethod
    def filter_by_location(cls, location):
        """
        A method to filter all photos based on the location in which they were taken
        """
        return cls.objects.filter(location = location)





