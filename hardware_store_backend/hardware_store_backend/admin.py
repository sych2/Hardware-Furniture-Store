from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

User = get_user_model()

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ['username', 'email', 'first_name', 'last_name', 'is_verified', 'is_staff']
    list_filter = ['is_staff', 'is_superuser', 'is_active', 'is_verified']
    
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {
            'fields': ('phone_number', 'address', 'city', 'postal_code', 
                      'country', 'date_of_birth', 'is_verified', 
                      'company_name', 'tax_id')
        }),
    )
    
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Additional Info', {
            'fields': ('email', 'phone_number', 'first_name', 'last_name')
        }),
    )