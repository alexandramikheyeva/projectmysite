from django.views import generic
from django.shortcuts import redirect, render
from django.urls import reverse_lazy, reverse
from django.views.generic import View
from cart.forms import ChangeStatusForm

from cart.models import Cart, BookInOrder

from bookshop.models import Book
from .models import Order
from . import models


# Create your views here.

class AddToCartView(View):
    def get(self, request, *args, **kwargs):
        user = request.user
        cart = Cart.objects.get(user=user)
        book_pk = kwargs.get("pk")
        book = Book.objects.get(pk=book_pk)
        if cart.check_if_book_already_in_cart(book):
            return redirect(to=reverse("bookshop:view-book", kwargs={
                "pk": book_pk
            }))
        book_in_cart = BookInOrder.objects.create(
            book=book,
            count=1,
        )
        cart.books.add(book_in_cart)
        return redirect(to=reverse("bookshop:view-book", kwargs={  
            "pk": book_pk
        }))


class CartView(generic.DetailView):
    model = models.Cart
    template_name = "cart/cart.html"

    def get_object(self):
        user = self.request.user
        if user.is_authenticated:
            return Cart.objects.get(user=user)
        return None

    def post(self, request, *args, **kwargs):
        cart = self.get_object()

        if "checkout" in request.POST:
            order = Order.objects.create(
                user=cart.user, 
                total_price=cart.get_total_price()
                )
            for book_in_cart in cart.books.all():
                order.books.add(book_in_cart)
            cart.clear_cart()

            return redirect('cart:view_cart')
        else:
            item_id = request.POST.get("item_id")
            count = request.POST.get("count")
            cart.update_count(item_id, count)
            return redirect('cart:view_cart')

    def remove_item(request, cart_id, item_id):
        cart = Cart.objects.get(id=cart_id)
        item = cart.books.get(id=item_id)
        item.delete()
        return redirect('cart:view_cart')
    
    def handle_cart(request):
      if request.method == "POST":
        cart = Cart.objects.get(id=request.POST.get('cart_id'))
        description=request.POST.get('description')
        print(description)
        if not description:
          description = ""
        order = Order.objects.create(
            user=cart.user, 
            total_price=cart.get_total_price(),
            description=description
        )
  
        for book in cart.books.all():
            book_obj = book.book
            if book_obj.counter_book == book.count:
                book_obj.counter_book -= book.count
                book_obj.active = 'N'
                book_obj.save()
            else:
                book_obj.counter_book -= book.count
                book_obj.save()
            order.books.add(book)
      
        cart.clear_cart()
        carts = Cart.objects.all()
        for cart in carts:
            cart.books.filter(book__active='N').delete()   
        return redirect('cart:view_cart')
    
    def order_details(request, order_id):
      order = Order.objects.get(id=order_id)
      if request.method == "POST":
          form = ChangeStatusForm(request.POST)
          if form.is_valid():     
              if request.user.is_superuser:
                  order.status = form.cleaned_data['status']
                  order.save()    
      else:
          form = ChangeStatusForm()          
      status_list = Order.STATUS      
      return render(
          request,
          'cart/order_details.html', {
              'order': order,
              'form': form,  
              'status_list': status_list                
          }
      )
    
    def orders_all(request):
      orders = Order.objects.all()
      return render(request, 'cart/orders_all.html', {'orders':orders})

    def clear_cart(self):
        self.books.clear()