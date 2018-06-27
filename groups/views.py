from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.contrib.auth.mixins import(
    LoginRequiredMixin,
    PermissionRequiredMixin
)
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.db import IntegrityError
from django.views import generic
from groups.models import Group, GroupMember
from . import models
