from django.contrib import admin
from .models import Realtor

class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'mvp', 'email', 'hired_date')
    list_display_links = ('id', 'name')
    list_editable = ('mvp',)
    search_fields = ('name', 'email')
    list_per_page = 25

admin.site.register(Realtor, RealtorAdmin)