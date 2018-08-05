from django.urls import path

from . import views

app_name = 'curriculum'
urlpatterns = [
    path('', views.CurriculumListView.as_view(), name='index'),
    path('<int:pk>/', views.CurriculumDetailView.as_view(), name='detail'),
    path('reading/<int:pk>/', views.ReadingDetailView.as_view(), name='reading_detail')
]
