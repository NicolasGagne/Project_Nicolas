from django.db import models

from django.utils import timezone

# Create your models here.

TYPE_CHOICES = (
    (1, "Un define"),
    (2, "Tool"),
    (3, "Aviation"),
    (4, "Interesting"),
    (5, "Motorcycle"),
    (6, "Programation"),
)

# Model for the Bookmark site
class Bookmark(models.Model):
    created = models.DateTimeField(default=timezone.now)
    last_active = models.DateTimeField(default=timezone.now)
    last_check = models.DateTimeField(default=timezone.now)
    site_link = models.URLField(max_length=250, default='url', unique=True)
    title = models.CharField(max_length=25, default='Site name', unique=True)
    description = models.TextField(max_length=144, default= 'Short description')
    type = models.IntegerField(choices=TYPE_CHOICES, default=1)
