from django import forms

from cart.models import Order

class ChangeStatusForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['status']