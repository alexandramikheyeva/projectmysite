from django.http import Http404
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from cart.models import Order
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView
from . models import Account, Address
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserChangeForm
from django import forms
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver



@login_required
def profile(request):
    user = request.user
    try:
        account = Account.objects.get(user=user)
    except Account.DoesNotExist:
        account = None
    orders = Order.objects.filter(user=user)
    groups = user.groups.all()
    context = {'user': user, 'account': account, 'orders': orders, 'groups': groups}
    return render(request, 'user_profile/profile.html', context)


User = get_user_model()

class AccountUpdateForm(UserChangeForm, forms.ModelForm):
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)
    country = forms.CharField(max_length=30, required=False)
    city = forms.CharField(max_length=20, required=False)
    zip_code = forms.DecimalField(max_digits=15, decimal_places=0, required=False)
    address1 = forms.CharField(max_length=50, required=False)
    address2 = forms.CharField(max_length=50, required=False)
    class Meta:
        model = Account
        fields = ['phone', 'view_personal_info', 'gender', 'address']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fieldname in UserChangeForm.base_fields:
            self.fields[fieldname] = UserChangeForm.base_fields[fieldname]
        self.fields['first_name'].initial = self.instance.user.first_name
        self.fields['last_name'].initial = self.instance.user.last_name
        self.fields['email'].initial = self.instance.user.email

        if self.instance.address:
            self.fields['country'].initial = self.instance.address.country
            self.fields['city'].initial = self.instance.address.city
            self.fields['zip_code'].initial = self.instance.address.zip_code
            self.fields['address1'].initial = self.instance.address.address1
            self.fields['address2'].initial = self.instance.address.address2
        del self.fields['last_login']
        del self.fields['password']
        del self.fields['address']
        del self.fields['is_superuser']
        del self.fields['groups']
        del self.fields['user_permissions']
        del self.fields['is_staff']
        del self.fields['is_active']
        del self.fields['date_joined']
        
    def save(self, commit=True):
        user = self.instance.user
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        account = super().save(commit=False)
        if self.cleaned_data['country']:
            if not account.address:
                account.address = Address.objects.create()
            account.address.country = self.cleaned_data['country']
            account.address.city = self.cleaned_data['city']
            account.address.zip_code = self.cleaned_data['zip_code']
            account.address.address1 = self.cleaned_data['address1']
            account.address.address2 = self.cleaned_data['address2']
            account.address.save()

        if commit:
            account.save()
        return account


class AccountUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy("staff:login")
    model = Account
    form_class = AccountUpdateForm
    template_name = 'user_profile/update_profile.html'
    success_url = reverse_lazy('user_profile:profile')

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.user != self.request.user:
            raise Http404
        return obj
    

    @receiver(post_save, sender=User)
    def create_account(sender, instance, created, **kwargs):
      if created:
          address = Address.objects.create()
          Account.objects.create(user=instance, address=address)
          group = Group.objects.get(name='Customers')
          instance.groups.add(group)
          

    @receiver(post_save, sender=User)
    def save_account(sender, instance, **kwargs):
        try:
            instance.account.save()
        except Account.DoesNotExist:
            address = Address.objects.create()
            Account.objects.create(user=instance, address=address)