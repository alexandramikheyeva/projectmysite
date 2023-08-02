from django.shortcuts import render
from django.shortcuts import render, redirect
from django.views.generic import ListView, UpdateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserChangeForm
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CustomerProfile, Address
from django.contrib.auth.models import User
from django.db import models
from cart.models import Order
from .forms import CustomerProfileForm, AddressForm

# Create your views here.


# class ProfileView(LoginRequiredMixin, ListView):
#     template_name = 'profile.html'
#     context_object_name = 'profile'

    # def get_queryset(self):
    #     return CustomerProfile.objects.filter(user=self.request.user)
    
    
#Переход в  профиль
@login_required
def get_profile(request):
    user=request.user
    print("USER", user)
    orders = Order.objects.filter(user=user)
    print("ORDERS", orders)
    profile, created = CustomerProfile.objects.get_or_create(user=user)
    profile.address, created =Address.objects.get_or_create(user=user)
    print("PROFILE", CustomerProfile.objects.get(user=request.user))
    print("PROFILE", orders.all)
    print("PROFILE", profile.address)
    # groups= profile.group
    # print("GROUPS", groups)
    # context = {'user': user, 'profile': profile, 'orders': orders, 'groups': groups}
    context = {'user': user, 'profile': profile, 'orders': orders}
    return render(request, 'profile/profile.html', context) 



@login_required
def profile(request):
    user = request.user
    orders = Order.objects.filter(user=user)
    profile, created = CustomerProfile.objects.get_or_create(user=user)
    address, created = Address.objects.get_or_create(user=user)

    if request.method == 'POST':
        address_form = AddressForm(request.POST, instance=address)
        profile_form = CustomerProfileForm(request.POST, instance=profile)
        
        if address_form.is_valid() and profile_form.is_valid():
            address = address_form.save()
            profile = profile_form.save(commit=False)
            profile.address = address
            profile.save()
            return redirect('profile:profile_view')
    else:
        address_form = AddressForm(instance=address)
        profile_form = CustomerProfileForm(instance=profile)
    
    context = {
        'user': user,
        'profile': profile,
        'orders': orders,
        'address_form': address_form,
        'profile_form': profile_form
    }
    
    return render(request, 'profile/edit_profile.html', context) 

# def profile(request):
#     user = CustomerProfile.objects.get(user=request.user)
#     print("4/1", user)
#     address = Address.objects.get(user=request.user)
#     print("4/2", address)
#     print("4/3", user.profile)
#     profile_data = {
#         'email_profile': user.email_profile,
#         'first_profile_name': user.first_profile_name,
#         'last_profile_name': user.last_profile_name,
#         'phone': user.phone,
#         'group': user.group,
#         'address': address,
#         'additional_info': user.additional_info,
#     }
    
#     if request.method == 'POST':
#         profile_form = UserProfileForm(request.POST, user=user, instance=user.address)
#         address_form = AddressForm(request.POST, instance=address)
        
#         if profile_form.is_valid() and address_form.is_valid():
#             profile_form.save()
#             address_form.save()
            
#             return redirect('profile')
#     else:
#         profile_form = UserProfileForm(user=user, instance=user.address, initial=profile_data)
#         address_form = AddressForm(instance=address)
        
#     return render(request, 'profile/profile.html', {'profile_form': profile_form, 'address_form': address_form})







# @login_required
# def edit_profile(request):
#     user = request.user
#     print("1/1", user)
#     profile = CustomerProfile.objects.get(user=user)
#     print("1/2", profile.user)
#     print("1/2/2", profile.address)

#     if request.method == 'POST':
#         form = UserProfileForm(request.POST, instance=request.user)
#         if form.is_valid():
#             form.save()
#             return redirect('profile:profile_edit')
#     else:
#         form = UserProfileForm(instance=profile)

#     context = {
#         'form': form
#     }
#     return render(request, 'profile/edit_profile.html', context)  










# def get_profile(self, item_id):
#     print(item_id)
#     profile = CustomerProfile.objects.filter(user=self.user)
#     return 'profile/profile.html', profile

# class OrderHistoryView(LoginRequiredMixin, ListView):
#     template_name = 'order_history.html'
#     context_object_name = 'orders'

#     def get_queryset(self):
#         return self.request.user.orders.all()


# @login_required
# def other_customers_profile_view(request):
#     customer_id = request.GET.get('customer_id')
#     customer_profile = CustomerProfile.objects.get(id=customer_id)
#     context = {'customer_profile': customer_profile}
#     return render(request, 'other_customers_profile.html', context)


# class EditProfileView(LoginRequiredMixin, UpdateView):
#     model = CustomerProfile
#     fields = ['first_name', 'last_name', 'email']
#     template_name = 'edit_profile.html'
#     success_url = '/profile'
#     context_object_name = 'profile'


# class EditOrderView(LoginRequiredMixin, UpdateView):
#     model = models.Order
#     fields = ['status']
#     template_name = 'edit_order.html'
#     success_url = '/order_history'
#     context_object_name = 'order'


# @login_required
# def cancel_order_view(request, order_id):
#     order = request.user.orders.get(id=order_id)
#     if order.status != 'Cancelled':
#         order.status = 'Cancelled'
#         order.save()
#     return redirect('order_history')


# @receiver(post_save, sender=User)
# def create_customer_profile(sender, instance, created, **kwargs):
#     if created:
#         CustomerProfile.objects.get_or_create(user=instance)


# @receiver(post_save, sender=User)
# def save_customer_profile(sender, instance, **kwargs):
#     instance.customer_profile.save()
