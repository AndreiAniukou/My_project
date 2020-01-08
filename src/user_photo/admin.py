from django.contrib import admin
from . import models UserPhoto
# Register your models here.

class UserPhotoAdmin(admin.ModelAdmin):
    list_display = ['description', 'rating', 'slug', 'url']
    prepopulated_fields = {'slug': ['description']}

admin.site.register(UserPhoto, UserPhotoAdmin)