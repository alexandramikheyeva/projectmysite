from django.contrib import admin
from .models import Account
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

from . import models
# Register your models here.



class AccountInLine(admin.StackedInline):
    model = Account
    can_delete = False
    verbose_name_plural = 'Account'


class CustomizedUserAdmin(UserAdmin):
    inlines = (AccountInLine, )


admin.site.unregister(User)
admin.site.register(models.User, CustomizedUserAdmin)
admin.site.register(models.Address)