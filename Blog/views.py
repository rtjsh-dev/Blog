from django.shortcuts import render, get_object_or_404, redirect
from Blog_app.models import Category,Blog
from assignment.models import About
from django.db.models import Q
from .forms import UserRegistration
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth

def home(request):
  try:
    about = About.objects.get()
  except:
    about = None
  # print(about)
  category = Category.objects.all()
  featuered_post = Blog.objects.filter(is_Featured=True, status="Published").order_by('-updated_At')
  posts = Blog.objects.filter(is_Featured=False, status="Published")
  context = {
    'about': about,
    'featured_post' : featuered_post,
    'category': category,
    'posts':posts,
  }
  return render(request, 'home.html', context,)

def blog(request, slug):
  single_post = get_object_or_404(Blog , slug=slug, status="Published")
  context = {
    "blog": single_post,
  }
  return render(request, 'Blogs.html', context)

def search(request):
  keyword = request.GET.get("keyword")
  # print(keyword)
  blog = Blog.objects.filter(Q(title__icontains=keyword) | Q(short_description__icontains=keyword)| Q(blog_body__icontains=keyword), status="Published")
  # print(blog)
  context  = {
    "keyword": keyword,
    "blog": blog,
  }
  return render(request, 'search.html', context)

def register(request):
  if request.method == 'POST':
    form = UserRegistration(request.POST)
    if form.is_valid():
      form.save()
      return redirect('register')
  else:
    form = UserRegistration()
  context = {
    'form': form,
  }
  return render(request, 'register.html', context)

def login(request):
  if request.method == 'POST':
    form = AuthenticationForm(request, request.POST)
    if form.is_valid():
      username = form.cleaned_data['username']
      password = form.cleaned_data['password']
      user = auth.authenticate(username=username, password=password)
      if user is not None:
        auth.login(request,user)
      return redirect('home')
  form = AuthenticationForm()
  context = {
    'form': form,
  }
  return render(request, 'login.html', context)

def logout(request):
  auth.logout(request)
  return redirect('home')