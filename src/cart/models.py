from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.dispatch import receiver
from book.models import Book
from user_profile.models import CustomerProfile

# Create your models here.

#Модель(первая часть корзины), из нее берем книги(из книг вытягивать имя, цену), количество
class BookInCart(models.Model):
    # Через переменную book связываемся с моделью Book для вытягивания нужных нам данных
    book = models.ForeignKey(
        to=Book, 
        on_delete=models.CASCADE
    )
    # Водим переменную count, которая представляет собой количество книг в корзине(для дальнейшего подсчета общей стоимости корзины)
    count = models.PositiveIntegerField(
        default=1
    ) 
    
    def calculate_total_price(book_in_cart):
        return book_in_cart.count * book_in_cart.book.price 
    
#Модель(вторая ччасть корзины), в ней определенный пользователь которому присвоена определенная корзина
class Cart(models.Model):
    user = models.OneToOneField(
        to=User, 
        on_delete=models.PROTECT, 
        null=True,
        blank=True
        )
    # переменная books вытягивает из модели BookInCart все добавленые книги(книги добавленные в корзину), 
    # для дальнейшего подсчета стоимости корзины
    books = models.ManyToManyField(
        to=BookInCart,
        verbose_name="Books in cart",
        blank=True
    )
    created = models.DateTimeField(
        verbose_name="Created",
        auto_now_add=True,
        auto_now=False
    )
    updated = models.DateTimeField(
        verbose_name="Updated",
        auto_now_add=False,
        auto_now=True
    )
    
    phone = models.CharField(
        max_length=15, 
        null=True, 
        blank=True, 
        default=None
    )
    
    cart_comment = models.CharField(
        max_length=255,
        verbose_name="Cart comment",
        null=True, 
        blank=True,
        default=None
    )
    
    #  Сумарное количество книг в корзине
    @property
    def get_result_price_of_cart(self):
        total_price=0
        for book_in_cart in self.books.all():
            price = book_in_cart.book.price
            count = book_in_cart.count
            total_price+= price*count
        return total_price
    
    # Подсчет стоимости товарной позиции при изменении количества
    @property
    def update_count(self, item_id, count):
        book_in_cart = self.books.get(id=item_id)
        book_in_cart.count = count
        book_in_cart.save()
    
    @property
    def get_total_count_of_cart(self):
        total_count = 0
        for book_in_cart in self.books.all():
            total_count += book_in_cart.count
        return total_count
    # Очищает корзину при оформлении заказа
    @property
    def clear_cart(self):
        self.books.clear()
        return ...
    
    # Проверка на наличие книги в корзине, если нет, добавляем, если есть, +1
    def check_if_book_already_in_cart(self, book_to_check):
        for book_in_cart in self.books.all():
            checked_book= book_in_cart.book
            if checked_book == book_to_check:
                return True
           
    

class Order(models.Model):
    user = models.ForeignKey(
        # to=User,
        # verbose_name="Customer",
        # on_delete=models.CASCADE,
        # blank=False
        to=User, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True
        )
    books = models.ManyToManyField(
        to=BookInCart,
        verbose_name="Books in cart",
        blank=True
        )
           
    price = models.DecimalField(
        max_digits=12, 
        decimal_places=2, 
        default=0,
        blank=True
        )

    STATUS = (
        ('In process', 'In process'),
        ('Something wrong', 'Something wrong'),
        ('Ready', 'Ready'),
    )
    status = models.CharField(
        max_length=255,
        choices = STATUS,
        verbose_name="Order status",
        blank=True
    )
    created = models.DateTimeField(
        verbose_name="Created",
        auto_now_add=True,
        auto_now=False
    )
    updated = models.DateTimeField(
        verbose_name="Updated",
        auto_now_add=False,
        auto_now=True
    )
    
    cart_comment_in_order = models.CharField(
        max_length=255,
        verbose_name="Cart comment in order",
        null=True, 
        blank=True,
        default=None
    )

    def str(self):
        return f"Order {self.id} by {self.user.username} on {self.created_at}"
