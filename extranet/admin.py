from django.contrib import admin

from .models import CompanyCustomer, PrivateCustomer

# Register your models here.
admin.site.register(CompanyCustomer)
admin.site.register(PrivateCustomer)