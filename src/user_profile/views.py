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
