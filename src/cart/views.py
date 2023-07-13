from django.db import models
from django.shortcuts import render
from django.views import generic
from .models import Cart, Book, BookInCart
from django.shortcuts import redirect, render
from django.urls import reverse_lazy, reverse
from django.views.generic import View
from . import models
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import request
from django.contrib.auth.decorators import login_required
from user_profile.models import CustomerProfile

# Create your views here.

# Работа с моделью книги в корзине, процесс добавления книги в корзину, если 
# книги нет, ее добавляет в корзину, если книга есть, увеличивает количество в 
# корзине на 1 штуку
# Работа с моделью корзина, включает видимые методы

class CartView(generic.TemplateView):
    model = models.Cart
    template_name = "cart/cart_view.html"
    
    
    #Отображения содержимого корзины
    def get_context_data(self, **kwargs):
        pk = self.request.session.get("cart_id")
        print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
        context = super().get_context_data(**kwargs)
        print(context)
        user = self.request.user
        if user.is_anonymous:
            user = None
            cart, created = models.Cart.objects.get_or_create(pk=pk)
        elif user.is_authenticated:
            profile = models.CustomerProfile.objects.get_or_create(user=user)
            cart, created = models.Cart.objects.get_or_create(user=user)
            print("Phone", profile.phone)
            print("Cart comment", cart.cart_comment)
            cart.phone = profile.phone
            context["profile"] = profile
        # cart, created = models.Cart.objects.get_or_create(pk=pk)
        print(cart, 'asfasf')
        self.request.session['cart_id'] = cart.pk
        print("Cart pk is ", cart.pk)
        books_in_cart = cart.books.all()
        # print("print title", books_in_cart.book.title)
        for book in books_in_cart:
            print(book.book.quantity_available)
        # print(cart.books.book.quantity_available)
        # print(books_in_cart.book.title)
        context["cart"] = cart
        context["books_in_cart"] = books_in_cart
        # total_count=cart.get_total_count_of_cart
        # print(total_count)
        return context
    
    
    #Отображение всех заказов, если аноним, заказ из сессии
    def orders_all(request):
       
        user = request.user
        print("4.1", user)
        if user.is_anonymous:
            order_id=request.session['order_id']
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
     
     
    #Обновление количества книг
    def update_cart(request, cart_id, item_id):
        # if request.method == 'POST':
            print("1", cart_id)
            print("2", item_id)
            cart = models.Cart.objects.get(pk=cart_id)
            book_id = request.POST.get('item_id')
            print("3",request.POST.get('item_id'))
            count = int(request.POST.get('count'))
            print("4", int(request.POST.get('count')))
            book = cart.books.get(id=book_id)
            print(book.book.quantity_available)
            book.count = count
            book.save()
        # return redirect('cart:cart_view')
            return redirect('cart:cart_view')
    
    # Добавление номера телефона в корзину если аноним
    def update_phone(request, item_id):
        pk = request.session.get("cart_id")
        print("CARD ID", item_id)
        phone_number = request.POST.get('phone')
        print(phone_number)
        # cart, created = models.Cart.objects.get_or_create(pk=pk)
        cart = models.Cart.objects.get(pk=pk)
        cart.phone=phone_number
        cart.save()
        return redirect('cart:cart_view')  
    
    def make_comment(request, item_id):
        pk = request.session.get("cart_id")
        print("CARD ID", item_id)
        comment = request.POST.get('cart_comment')
        print("heehehhehheheheheh", comment)
        # cart, created = models.Cart.objects.get_or_create(pk=pk)
        cart = models.Cart.objects.get(pk=pk)
        cart.cart_comment=comment
        cart.save()
        return redirect('cart:cart_view')  
       
        
    #Удаление книги из корзины
    def delete_book(request, cart_id, item_id):
        cart = models.Cart.objects.get(pk=cart_id)
        print("2,1", cart)
        item = cart.books.get(id=item_id)
        print("2,2", item)
        item.delete()
        return redirect('cart:cart_view')
    
    
    #Создание заказа
    
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
                print("title", book_in_cart.book.title)
                print("ava quant", book_in_cart.book.quantity_available)
                print("count in order", book_in_cart.count)
                book_in_cart.book.quantity_available -= book_in_cart.count
                # book_in_cart.book.save()
                print(book_in_cart.book.is_active)
                if book_in_cart.book.quantity_available == 0:
                    book_in_cart.book.is_active = False
                print(book_in_cart.book.is_active)
                print("CAART COMENT", cart.cart_comment)
                print("title 2", book_in_cart.book.title)
                print("ava quant 2", book_in_cart.book.quantity_available)
                print("count in order 2", book_in_cart.count)
                book_in_cart.book.save()
                order.books.add(book_in_cart)
                cart.clear_cart
        print("CAART COMENT", cart.cart_comment)
        order.cart_comment_in_order = cart.cart_comment
        order.save()
        cart.cart_comment = None
        cart.save()
        self.session['order_id'] = order.pk
        print("order id", self.session['order_id'])
        # print("3.1", models.Cart.objects.get(pk=cart_id))
        # order = models.Order.objects.get_or_create(
        #     cart = models.Cart.objects.get(pk=cart_id),
        #     user=cart.user, 
        #     price=cart.get_result_price_of_cart)
        # # cart.clear_cart()
        # print(order[0].pk)
        # self.session['order_id'] = order[0].pk
        # print(self.session['order_id'])
        # cart.clear_cart()
        # self.session.pop('cart_id', None)
        return redirect('book:book_view_all.html')
 
     
# Добавление книги в корзину    
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
