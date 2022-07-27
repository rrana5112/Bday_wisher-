from django.contrib import admin
from .models import *


class PeopleAdmin(admin.ModelAdmin):
    list_display=['id','name','email','dob','category']
    search_fields=['name','email','dob']
    list_filter=['category']


class WishesTextAdmin(admin.ModelAdmin):
    list_display = ['category','text','time_sent']
    list_filter=['category']

admin.site.register(People,PeopleAdmin)
admin.site.register(WishesText,WishesTextAdmin)