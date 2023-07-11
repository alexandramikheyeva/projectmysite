from django.db import models
from django.contrib.auth import get_user_model
from django.db.models import Sum
from django.utils import timezone

from bookshop.models import Book

# Create your models here.

User = get_user_model()


class BookInOrder(models.Model):
    book = models.ForeignKey(to=Book, on_delete=models.CASCADE)
    count = models.IntegerField(default=1)
    
    def get_total_price_in_order(self):
        return self.count * self.book.book_price 


class Cart(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE, unique=True)
    books = models.ManyToManyField(to=BookInOrder, blank=True)

    def check_if_book_already_in_cart(self, book_to_check):
        for book_in_cart in self.books.all():
            book = book_in_cart.book
            if book == book_to_check:
                return True

    def get_total_price(self):
        total_price = 0
        for book_in_cart in self.books.all():
            count = book_in_cart.count
            price = book_in_cart.book.book_price
            total_price += price * count
        return total_price

    def get_total_count(self):
        total_count = 0
        for book_in_cart in self.books.all():
            count = book_in_cart.count
            total_count +=  count
        return total_count
    
    def get_grouped_price(self):
      grouped_price = []
      for book_in_cart in self.books.all().select_related('book').values('book_id', 'book__book_name', 'book__book_price').annotate(count=Sum('count')):
          count = book_in_cart['count']
          price = book_in_cart['book__book_price']
          book_name = book_in_cart['book__book_name']
          grouped_price.append({'book_name': book_name, 'count': count, 'price': price, 'total_price': count * price})
      return grouped_price
    
    def update_count(self, item_id, count):
        book_in_cart = self.books.get(id=item_id)
        book_in_cart.count = count
        book_in_cart.save()
    
    def clear_cart(self):
      self.books.clear()
    
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    books = models.ManyToManyField(to=BookInOrder, blank=True)
    description =  models.TextField(blank=True, null=True)

    STATUS = (
        ('В обработке', 'В обработке'),
        ('Выполняется', 'Выполняется'),
        ('Доставлено', 'Доставлено'),
        ('Отменен', 'Отменен'),
    )
    status = models.CharField(
        verbose_name = 'Статус заказа',
        max_length = 11,
        default= 'В обработке',
        choices = STATUS
    )
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def str(self):
        return f"Order {self.id} by {self.user.username} on {self.created_at}"     
     
    def get_total_count_in_order(self):
        total_count = 0
        for book_in_cart in self.books.all():
            count = book_in_cart.count
            total_count +=  count
        return total_count 