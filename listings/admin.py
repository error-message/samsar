from django.contrib import admin
from .models import Listing

class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'published', 'price', 'list_date','realtor')
    list_display_links = ('id', 'title')
    list_filter = ('realtor','city')
    list_editable = ('published', 'price')
    search_fields = ('title', 'description', 'state', 'city', 'address', 'zipcode', 'price')
    list_per_page = 25

admin.site.register(Listing, ListingAdmin)