from django.db import models
from datetime import date

# Create your models here.

class UserPhoto(models.Model):
    description = models.CharField(max_length=600,
                                   default="Write ur description here",
                                   verbose_name="Description")
    rating = models.IntegerField(default=0, max_value=5)
    slug = models.SlugField(max_length=60, unique=True)
    url = models.URLField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.description} - {self.slug[:10]}"

