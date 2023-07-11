from django.contrib import admin
from . import models

# Register your models here.

from .models import Cart, BookInOrder, Order

admin.site.register(BookInOrder)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "get_books", 
        "total_price",
        "status",
    )

    def get_books(self, obj):
        return "\n, ".join([str(book) for book in obj.books.all()])

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "get_total_price"
    )