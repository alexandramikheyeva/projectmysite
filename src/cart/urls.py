from django.urls import path
from . import views

app_name = 'cart'
urlpatterns = [
    path('book_add_to_cart/<int:pk>', views.AddBookToCart.as_view(), name='book_add_to_cart.html'),
    path('cart_view', views.CartView.as_view(), name='cart_view'),
    path('cart/update/<int:cart_id>/<int:item_id>/', views.CartUpdateView.update_cart, name='update_cart'),
    path('cart/update/<int:item_id>/', views.CartUpdateView.update_phone, name='update_phone'),
    path('cart/update_comment/<int:item_id>/', views.CartUpdateView.make_comment, name='comment'),
    path('cart/delete/<int:cart_id>/<int:item_id>/', views.CartUpdateView.delete_book, name='delete_book'),
    path('order/view/<int:cart_id>', views.CartUpdateView.create_order, name='order_view'),
    path("orders_all/", views.CartView.orders_all, name="orders_all"),
    # path('order/<int:cart_id>', views.OrderView.as_view(), name='order_view'),
    ]
    