from django.contrib import admin
from .models import ContactModel, BannerModel


@admin.register(BannerModel)
class BannerModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'collection', 'is_active']
    list_display_links = ['id', 'title']
    search_fields = ['title', 'collection']


@admin.register(ContactModel)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'email']
    list_display_links = ['id', 'email']
