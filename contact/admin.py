from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ['subject', 'email']
    search_fields = ['subject', 'email']

    class Meta:
        model = Contact


admin.site.register(Contact, ContactAdmin)
