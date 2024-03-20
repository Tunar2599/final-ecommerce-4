from django.contrib import admin
from .models import Contact
from .models import Category, BlogPost

# Register your models here.

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    fields = ['created', 'name', 'email', 'subject', 'message']
    readonly_fields = ['created']



admin.site.register(Category)
admin.site.register(BlogPost)

from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'view_count')
    list_filter = ('created_at',)
    search_fields = ('title', 'content')

admin.site.register(Post, PostAdmin)




