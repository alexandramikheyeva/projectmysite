from django.urls import include, path
from . import views

app_name = 'cart'

urlpatterns = [
  
      path("add_to_cart/<int:pk>/", views.AddToCartView.as_view(), name="add_to_cart"),
      path("cart/", views.CartView.as_view(), name="view_cart"),
      path("orders_all/", views.CartView.orders_all, name="orders_all"),
      path('checkout/', views.CartView.handle_cart, name='checkout'),
      path('cart/<int:cart_id>/update/<int:item_id>/', views.CartView.as_view(), name='update_item'),
      path('cart/<int:cart_id>/remove/<int:item_id>/', views.CartView.remove_item, name='remove_item'),
      path('order/<int:order_id>/', views.CartView.order_details, name='order_details'),
]