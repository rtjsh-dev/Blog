from django.shortcuts import get_object_or_404, redirect, render
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
  if request.method == "POST":
    form = CategoryForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('categories')
  form = CategoryForm()
  context = {
    'form': form, }
  return render(request, 'dashboard/add_category.html', context)

def edit_category(request, pk):
  category = get_object_or_404(Category, pk=pk)
  if request.method == "POST":
    form = CategoryForm(request.POST, instance=category)
    if form.is_valid():
      form.save()
      return redirect('categories')
  form = CategoryForm(instance=category)
  context = {
    'form': form,
    'category': category,
  }
  return render(request, 'dashboard/edit_category.html', context)


def delete_category(request, pk):
  category = get_object_or_404(Category, pk=pk)
  category.delete()
  return redirect('categories')
