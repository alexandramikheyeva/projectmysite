from django.db import models
from django.urls import reverse

# Create your models here.

class Autor(models.Model):
    autor_name = models.CharField(max_length = 50)
    autor_description = models.TextField(null = True, blank = True)

    def __str__(self) -> str:
        return self.autor_name
    
    def get_absolute_url(self):
        return reverse('directories:success-page')

class Genre(models.Model):
    genre_name = models.CharField(max_length = 50)
    genre_description = models.TextField(null = True, blank = True)

    def __str__(self) -> str:
        return self.genre_name
    
    def get_absolute_url(self):
        return reverse('directories:success-page')
    
class Publishing_House(models.Model):
    publishing_house_name = models.CharField(max_length = 50)
    publishing_house_description = models.TextField(null = True,blank = True)

    def __str__(self) -> str:
        return self.publishing_house_name
    
    def get_absolute_url(self):
        return reverse('directories:success-page')

class Series(models.Model):
    series_name = models.CharField(max_length = 100)
    series_description = models.TextField(null = True, blank = True)

    def __str__(self) -> str:
        return self.series_name
    
    def get_absolute_url(self):
        return reverse('directories:success-page')

class Book(models.Model):
    title  = models.CharField(max_length = 150)
    image = models.ImageField(blank = True, upload_to = "book/%Y/%m/%d/")
    price = models.DecimalField(max_digits=6, decimal_places=2)
    author = models.ForeignKey(Autor, on_delete = models.CASCADE)
    series = models.ForeignKey(Series, on_delete = models.PROTECT)
    genre = models.ForeignKey(Genre, on_delete = models.CASCADE)
    year_publishing = models.DateField(max_length = 50)
    page = models.DecimalField(max_digits = 6,decimal_places = 0,
        default = 0
    )
    BINDING = (
        ('Solid', 'solid'),
        ('Soft', 'soft'),
        ('Absent', 'absent'),
    )
    binding = models.CharField(max_length = 6, choices = BINDING)  
    FORMAT = (
        ('Super small', '84x108/64'),
        ('Small', '75x90/32'),
        ('Standart', '60x90/16'),
        ('Bigger', '70x108/16'),
        ('Big', '60x90/8'),
        ('Super big', '84x108/8'),
    )
    format_book = models.CharField(max_length = 12, choices = FORMAT)
    ISBN = models.CharField(max_length = 25)
    weight = models.DecimalField(max_digits = 6, decimal_places = 1,
        default = 0
    )
    age_restrictions = models.DecimalField(max_digits = 3, decimal_places = 0,
        default = 0
    )
    publishing_house = models.ForeignKey(
        Publishing_House,
        on_delete = models.PROTECT,
    )
    counter_book = models.DecimalField(max_digits = 7, decimal_places = 0,
        default = 0
    )
    ACTIVE = (
        ('Y', 'active'),
        ('N', 'inactive'),
    )

    active = models.CharField(max_length = 4, choices = ACTIVE)
    rating = models.DecimalField(max_digits = 2, decimal_places = 1,
        default = 0
    )

    def __str__(self) -> str:
        return self.book_name
    
    def get_absolute_url(self):
        return reverse('directories:success-page')
    
    def book_picture_medium(self):
        orig_url = self.book_image.url
        new_url = orig_url.split(".")
        picture_url = ".".join(new_url[:-1]) + "_250." + new_url[-1]
        return picture_url
    
    def book_picture_small(self):
        orig_url = self.book_image.url
        new_url = orig_url.split(".")
        picture_url = ".".join(new_url[:-1]) + "_40." + new_url[-1]
        return picture_url



