from django.db import models

# Create your models here.
class About(models.Model):
    heading = models.CharField(max_length=100)
    body = models.CharField(max_length=500)
    created_At =  models.DateTimeField(auto_now=True)
    updated_At =  models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.heading
    
    class Meta():
     verbose_name_plural = "About"


class SocialLinks(models.Model):
   platform = models.CharField(max_length=50)
   url = models.URLField(max_length=100)
   created_At = models.DateTimeField(auto_now=True)
   updated_At = models.DateTimeField(auto_now_add=True)

   def __str__(self):
        return self.platform
    
   class Meta():
      verbose_name_plural = "Social Links"