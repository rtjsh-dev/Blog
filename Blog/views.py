from django.shortcuts import render
from Blog_app.models import Category,Blog

def home(request):
  category = Category.objects.all()
  featuered_post = Blog.objects.filter(is_Featured=True, status="Published").order_by('-updated_At')
  posts = Blog.objects.filter(is_Featured=False, status="Published")
  # print(posts)
  # print(featuered_post)
  context = {
    'featured_post' : featuered_post,
    'category': category,
    'posts':posts,
  }
  return render(request, 'home.html', context,)