from django.contrib import admin

# Register your models here.

from .models import App, Country

admin.site.register(App)

admin.site.register(Country)
