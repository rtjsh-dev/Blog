from django.shortcuts import render
from Blog_app.models import Category, Blog
from django.contrib.auth.decorators import login_required
from .forms import CategoryForm 
# Create your views here.
@login_required(login_url='login')
def dashboard(request):
  categories = Category.objects.all()
  blogs = Blog.objects.all()
  context = {
    'categories': categories,
    'blogs': blogs,
    'categories_count': categories.count(),
    'blogs_count': blogs.count()
  }
  return render(request, 'dashboard/dashboard.html', context)

def categories(request):
  return render(request, 'dashboard/categories.html')

def add_category(request):
  form = CategoryForm()
  context = {
    'form': form, }
  return render(request, 'dashboard/add_category.html')