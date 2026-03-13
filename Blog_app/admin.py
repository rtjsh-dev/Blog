from django.contrib import admin
from .models import Category, Blog
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
  list_display = ['id', 'category_name', 'created_At', 'updated_At']
  ordering = ['id']

class BlogAdmin(admin.ModelAdmin):
  list_display = ['id', 'title', 'category', 'author', 'status','is_Featured','category_id','author_id']
  prepopulated_fields = {'slug': ('title',)}
  ordering = ['id']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Blog, BlogAdmin)