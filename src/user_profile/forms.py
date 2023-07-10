from django import forms
from .models import CustomerProfile, Address
from django.forms.models import modelform_factory

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ('country', 'city', 'postal_code', 'address_line_1', 'address_line_2')

class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model = CustomerProfile
        fields = ('email_profile', 'first_profile_name', 'last_profile_name', 'phone', 'group', 'additional_info')

