from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Blog, Category

# Create your views here.
def post_by_category(request, category_id):
  category = get_object_or_404(Category, pk=category_id)
  category_post = Blog.objects.filter(category=category, status="Published")
  context = {
    "category": category,
    "category_post": category_post,
  }
  return render(request, 'post_by_category.html', context)