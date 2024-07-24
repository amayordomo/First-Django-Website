from django.contrib import admin
from .models import contact_list, contact_form

# Register your models here.
admin.site.register(contact_list)
admin.site.register(contact_form)