from django.contrib import admin

# Register your models here.

from .models import *
admin.site.register(Stocks)
admin.site.register(Trader)
admin.site.register(Order)
admin.site.register(Profile)