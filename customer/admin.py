from django.contrib import admin
from .models import Customer_info

@admin.register(Customer_info)
class CustomerInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'active', 'date_created')
    search_fields = ('name', 'email')
    list_filter = ('active',)



