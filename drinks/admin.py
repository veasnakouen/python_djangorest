from django.contrib import admin

from .models import Drink,Post

class DrinkAdmin(admin.ModelAdmin):
    list_display = ['id','name','description']
    search_fields = ['name']

class PostAdmin(admin.ModelAdmin):
    list_display = ['id','title','author',"email"]
    search_fields = ['title']

admin.site.register(Drink,DrinkAdmin)
admin.site.register(Post,PostAdmin)