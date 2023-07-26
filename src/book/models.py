from django.db import models
from directories.models import Author, Genres, Series, Publishing
from django.urls import reverse_lazy
from django.urls import reverse
# Create your models here.

class Book(models.Model):
    # Название книги
    title = models.CharField(
        max_length=255,
        verbose_name="Book title"
    )

    # Фото обложки
    cover_image = models.ImageField(
        upload_to='book_images/', 
        blank=True,
        verbose_name="Book image"
    )

    # Цена (BYN)
    price = models.DecimalField(
        max_digits = 8, 
        decimal_places = 2,
        default = 1,
        verbose_name="Book price"
    )

    # Авторы книги (может содержать несколько авторов) - справочник
    authors = models.ForeignKey(
        to = Author,
        on_delete=models.CASCADE,
        verbose_name="Book author"
    )

    # Серия - справочник
    series = models.ForeignKey(
        to=Series, 
        on_delete=models.CASCADE,
        verbose_name="Book series"
    )

    # Жанры (один или несколько жанров) - справочник
    genres = models.ForeignKey(
        to = Genres,
        on_delete=models.CASCADE,
        verbose_name="Book genre"
    )

    # Год издания
    publication_year = models.DateField(
        verbose_name="Publication year"
        
    )

    # Страниц
    pages = models.PositiveIntegerField(
        verbose_name="Number of pages"
        
        
    )

    # Переплет
    BINDING = (
        ('Soft', 'soft'),
        ('Solid', 'solid'),
    )
    
    binding = models.CharField(
        verbose_name = 'Tipe of binding',
        max_length=255,
        choices = BINDING
    )

    #  Формат
    FORMAT = (
        ('A3', '100*100'),
        ('A4', '200*200'),
    )
    format = models.CharField(
        max_length=255,
        choices = FORMAT,
        verbose_name="Book Format"
    )

    #  ISBN
    isbn = models.CharField(
        max_length=255,
        verbose_name="ISBN"
        )

    #  Вес (гр)
    weight = models.PositiveIntegerField(
        verbose_name="Weight"
    )

    #  Возрастные ограничения
    age_limit = models.CharField(
        max_length=255,
        verbose_name="Age limit"
    )

    #  Издательство - справочник
    publisher = models.ForeignKey(
        to = Publishing, 
        on_delete=models.CASCADE,
        verbose_name="Publisher"
    )

    #  Количество книг в наличии
    quantity_available = models.PositiveIntegerField(
        verbose_name="Count"
    )

    #  Активный (доступен для заказа, Да/Нет)
    is_active = models.BooleanField(
        default=True,
        verbose_name="Activity"
    )

    #  Рейтинг (0 - 10)
    RATING = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
    )
    rating = models.CharField(
        choices = RATING,
        max_length=255,
        verbose_name="Rating"
    )

    #  Дата внесения в каталог
    date_added = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Date of adding"
    )

    #  Дата последнего изменения карточки
    date_updated = models.DateTimeField(
        auto_now=True,
        verbose_name="Date of changing"
    )
    
    def __str__(self) -> str:
        return self.title
    
    # def get_absolute_url(self):
    #     return reverse_lazy('hp:success.html')
    
    def get_absolute_url(self):
        return reverse('book:book_detail.html', args=[str(self.id)])