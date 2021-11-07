from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib import auth
from django.utils.translation import gettext_lazy as _


def blog_image_upload(instance, filename):
    return "media/{}".format(filename)

class Eyeimage(models.Model):
    image = models.ImageField( blank=True, upload_to=blog_image_upload)
