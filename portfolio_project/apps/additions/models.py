from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.core.validators import EmailValidator


# Create your models here.
class Contact(models.Model):
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.email

class Tool(models.Model):
    name = models.CharField(max_length=255)
    tool_num = models.IntegerField(null=True, default=0)
    description = models.TextField()
    image = models.ImageField(
        upload_to='tools/',
        blank=True,
        default='tools/no-image.jpg'
    )
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("tool_detail", kwargs={'slug':self.id})


class TravelPhoto(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(
        upload_to='travel_photos/',
        blank=True,
        default='no-image.jpg'
    )

    def __str__(self):
        return self.title.title()
