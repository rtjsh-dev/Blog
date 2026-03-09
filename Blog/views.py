from django.shortcuts import render
from Blog_app.models import Category

def home(request):
  category = Category.objects.all()
  context = {
    'category': category
  }
  return render(request, 'home.html', context,)