from django.shortcuts import render, get_object_or_404
from Blog_app.models import Category,Blog
from assignment.models import About

def home(request):
  try:
    about = About.objects.get()
  except:
    about = None
  # print(about)
  category = Category.objects.all()
  featuered_post = Blog.objects.filter(is_Featured=True, status="Published").order_by('-updated_At')
  posts = Blog.objects.filter(is_Featured=False, status="Published")
  # print(posts)
  # print(featuered_post)
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