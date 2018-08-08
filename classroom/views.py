from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, render
from django.views import generic

from .models import Instance, Event

class ClassroomIndexView(LoginRequiredMixin, generic.ListView):
    model = Instance

class InstanceDetailView(LoginRequiredMixin, generic.DetailView):
    model = Instance

class EventDetailView(LoginRequiredMixin, generic.DetailView):
    model = Event
