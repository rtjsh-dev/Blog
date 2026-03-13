from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
  category_name = models.CharField(max_length=100, unique=True)
  created_At = models.DateTimeField(auto_now_add=True)
  updated_At = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.category_name
  
  class Meta():
    verbose_name_plural = "Categories"

STATUS_CHOICES = (
  ("Draft", "Draft"),
  ("Published", "Published")
)

class Blog(models.Model):
  title = models.CharField(max_length=100, unique=True)
  slug = models.SlugField(max_length=100, blank=True, unique=True)
  category = models.ForeignKey(Category, on_delete=models.CASCADE)
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  featured_At = models.ImageField(upload_to='uploads/%Y/%m/%d')
  is_Featured = models.BooleanField(default=False)
  short_description = models.TextField(max_length=200)
  blog_body = models.TextField(max_length=1000)
  status = models.CharField(max_length=20, choices=STATUS_CHOICES,default="Draft")
  created_At = models.DateTimeField(auto_now_add=True)
  updated_At = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.title
