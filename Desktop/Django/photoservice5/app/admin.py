from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Photo

class PhotoAdmin(admin.ModelAdmin):
    list_display=('id','title')
    list_display=('id','title')

admin.site.register(Photo,PhotoAdmin)