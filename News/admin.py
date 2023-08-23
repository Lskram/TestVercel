from django.contrib import admin
from . import models
# Register your models here.
@admin.register(models.Author)
class AutherAdmin(admin.ModelAdmin):
    list_display=[
        'frist_mane',
        'Lest_Name',
        'rank',
        
    ]
@admin.register(models.News)
class AutherAdmin(admin.ModelAdmin):
    list_display=[
        'Author',
        'title',
        'content',
        'time_date',
        'immage',
        
    ]