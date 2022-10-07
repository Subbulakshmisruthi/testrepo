
from django.db import models

# Create your models here.

class image(models.Model):
    image = models.ImageField(null=True,blank=False)


