from cart.models import Cart


class ShoppingCartMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        number_of_items_in_cart = 0
        user = request.user

        if user and user.is_authenticated:
            cart = Cart.objects.get(user=user)
            request.cart_id = cart.id
            number_of_items_in_cart = cart.books.count()
        request.number_of_items_in_cart = number_of_items_in_cart
        return self.get_response(request)