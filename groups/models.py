from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.text import slugify
from django import template
#from accounts.models import User
from django.contrib.auth import get_user_model
User = get_user_model()

register = template.Library
# Create your models here


class Group(models.Model):
    '''
    This will initialize a class which will be called
    whenever a new group object is created
    '''
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(allow_unicode=True, unique=True)
    location = models.TextField(default='', blank=True)
    location_html = models.TextField(editable=False, default='', blank=True)
    members = models.ManyToManyField(User, through='GroupMember')
