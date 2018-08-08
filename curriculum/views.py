from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import get_object_or_404, render
from django.views import generic

from .models import Reading, Curriculum

class CurriculumListView(PermissionRequiredMixin, generic.ListView):
    permission_required = 'curriculum.can_view'
    model = Curriculum

class CurriculumDetailView(PermissionRequiredMixin, generic.DetailView):
    permission_required = 'curriculum.can_view'
    model = Curriculum

class ReadingDetailView(PermissionRequiredMixin, generic.DetailView):
    permission_required = 'curriculum.can_view'
    model = Reading
