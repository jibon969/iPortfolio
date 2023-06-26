from django.contrib import admin
from .models import User
# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'date_of_birth', 'gender', 'contact_number']
    search_fields = ['first_name', 'last_name', 'email', 'date_of_birth', 'gender', 'contact_number']
    list_per_page = 20

    class Meta:
        model = User


admin.site.register(User, UserAdmin)

