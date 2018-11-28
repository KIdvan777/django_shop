from django.contrib import admin

# Register your models here.

from .models import Header, Country

admin.site.register(Header)

admin.site.register(Country)
