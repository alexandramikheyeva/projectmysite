from django.shortcuts import render
from django.db import models
from django.views import generic
from .models import Cart, Book, BookInCart
from django.shortcuts import redirect, render
from django.urls import reverse_lazy, reverse
from django.views.generic import View
from . import models
from django.http import JsonResponse
from django.http import request

# Create your views here.

class CartView(generic.TemplateView):
    model = models.Cart
    template_name = "cart/cart_view.html"


    def get_context_data(self, **kwargs):
        pk = self.request.session.get("cart_id")
        print("Hello")
        context = super().get_context_data(**kwargs)
        user = self.request.user
        if user.is_anonymous:
            user = None
            cart, created = models.Cart.objects.get_or_create(pk=pk)
        else: cart, created = models.Cart.objects.get_or_create(user=user)
        print(cart, 'asfasf')
        books_in_cart = cart.books.all()
        context["cart"] = cart
        context["books_in_cart"] = books_in_cart
        return context
    def orders_all(request):
        order_id=request.session['order_id']
        print("order id", order_id)
        user = request.user
        print("4.1", user)
        if user.is_anonymous:
            print("anonimus part orders all")
            user=None
            orders = models.Order.objects.filter(pk=order_id)
        else: 
            print("auth order view")
            orders = models.Order.objects.filter(user=user)
            print(orders)
        return render(request, 'cart/orders_all.html', {'orders':orders})

class CartUpdateView(generic.DetailView):
    model = models.Cart
    template_name = "cart/cart_view.html"

    def update_cart(request, cart_id, item_id):
            print("1", cart_id)
            print("2", item_id)
            cart = models.Cart.objects.get(pk=cart_id)
            book_id = request.POST.get('item_id')
            print("3",request.POST.get('item_id'))
            count = int(request.POST.get('count'))
            print("4", int(request.POST.get('count')))
            book = cart.books.get(id=book_id)
            book.count = count
            book.save()
            return redirect('cart:cart_view')
    
    def update_phone(request, item_id):
        pk = request.session.get("cart_id")
        print("CARD ID", item_id)
        phone_number = request.POST.get('phone')
        print(phone_number)
        cart = models.Cart.objects.get(pk=pk)
        cart.phone=phone_number
        cart.save()
        return redirect('cart:cart_view')  
    
    def delete_book(request, cart_id, item_id):
        cart = models.Cart.objects.get(pk=cart_id)
        print("2,1", cart)
        item = cart.books.get(id=item_id)
        print("2,2", item)
        item.delete()
        return redirect('cart:cart_view')
    
    def create_order(self, cart_id):
        order_id = self.session.get('order_id')
        print(order_id)
        cart = models.Cart.objects.get(pk=cart_id)
        user = self.user
        print("4.1", user)
        if user.is_anonymous:
            print("anonimus part orders all")
            user=None
            order = models.Order.objects.create(user=None, price=cart.get_result_price_of_cart)
        else: order = models.Order.objects.create(user=user, price=cart.get_result_price_of_cart)
        for book_in_cart in cart.books.all():
                print(book_in_cart.book.title)
                print(book_in_cart.count)
                order.books.add(book_in_cart)
                cart.clear_cart
        self.session['order_id'] = order.pk
        print("order id", self.session['order_id'])
        return redirect('book:book_view_all.html')

class AddBookToCart(generic.DetailView):
    def get(self, request, *args, **kwargs):
        order_id = request.session.get('order_id')
        print(order_id)
        pk = self.request.session.get("cart_id")
        print(self.request.session.get("cart_id"))
        user = self.request.user
        print(user)
        if user.is_anonymous:
            user=None
            print("заходит в цикл анонимус")
            print(pk, type(pk))
        # if user is None:
            # cart = models.Cart.objects.create(user=user)
            cart, created = models.Cart.objects.get_or_create(pk=pk)
            print("заходит в циклпк из нон")
            self.request.session['cart_id'] = cart.pk  
            print(self.request.session['cart_id'])
        elif request.user.is_authenticated:
            print("here is auntificated")
            cart, created = models.Cart.objects.get_or_create(user=user)
        book_pk = kwargs.get("pk")
        book = models.Book.objects.get(pk=book_pk)
        if cart.check_if_book_already_in_cart(book):
            book_in_cart = BookInCart.objects.get(cart=cart, book=book)
            book_in_cart.count += 1
            book_in_cart.save()
            return redirect(to=reverse("book:book_detail.html", kwargs={
                "pk": book_pk
            }))
        else:
            book_in_cart = BookInCart.objects.create(
            book=book,
            count=1,
        )
            cart.books.add(book_in_cart)
        return redirect(to=reverse("book:book_detail.html", kwargs={  
            "pk": book_pk
        }))
