# admin.py
from django.contrib import admin
from .models import PhoneNumber, Category, Sim
from .forms import PhoneNumberForm


# Register the models with the admin
admin.site.register(PhoneNumber)
admin.site.register(Category)
admin.site.register(Sim)
