from django.contrib import admin
from .models import Information, Contact
# Register your models here.

admin.site.register(Information)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'subject']