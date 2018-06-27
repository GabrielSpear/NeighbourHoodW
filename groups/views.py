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

# Create your views here.


class CreateGroup(LoginRequiredMixin, generic.CreateView):
    fields = ("name", "location")
    model = Group


class SingleGroup(generic.DetailView):
    model = Group


class ListGroups(generic.ListView):
    model = Group
    context_object_name = 'all_groups'

    def get_queryset(self, *args, **kwargs):
        qs = Group.objects.all()
        query = self.request.GET.get("q", None)
        if query is not None:
            qs = qs.filter(name__icontains=query)
        return qs

class JoinGroup(LoginRequiredMixin, generic.RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        return reverse("groups:single", kwargs={"slug": self.kwargs.get("slug")})

    def get(self, request, *args, **kwargs):
        group = get_object_or_404(Group, slug=self.kwargs.get("slug"))

        try:
            GroupMember.objects.create(user=self.request.user, group=group)

        except IntegrityError:
            messages.warning(self.request, ("Warning, already a member of {}".format(group.name)))

        else:
            messages.success(
                self.request, "You are now a member of the {} group.".format(group.name))

        return super().get(request, *args, **kwargs)
