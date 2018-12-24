from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAmin(admin.ModelAdmin):
    list_display = ['title', 'is_public', 'updated_at']

    
