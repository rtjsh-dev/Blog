from .models import Category
from assignment.models import SocialLinks
def getCategory(request):
  categories = Category.objects.all()
  return dict(categories=categories)

def getsocialLinks(request):
  sociallinks = SocialLinks.objects.all()
  return dict(sociallinks = sociallinks)