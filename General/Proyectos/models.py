import uuid
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models.signals import pre_save
from django.utils.text import slugify

class Proyecto(models.Model):
    nombre = models.CharField(max_length=250)
    scrum = models.ForeignKey(User, on_delete=models.PROTECT)
