from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, render
from django.views import generic

from .models import Reading, Curriculum

class CurriculumListView(LoginRequiredMixin, generic.ListView):
    model = Curriculum

class CurriculumDetailView(LoginRequiredMixin, generic.DetailView):
    model = Curriculum

class ReadingDetailView(LoginRequiredMixin, generic.DetailView):
    model = Reading
