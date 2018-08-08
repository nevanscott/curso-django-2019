from django.urls import path

from . import views

app_name = 'classroom'
urlpatterns = [
    path('', views.ClassroomIndexView.as_view(), name='index'),
    path('<int:pk>/', views.InstanceDetailView.as_view(), name='instance'),
    path('event/<int:pk>/', views.EventDetailView.as_view(), name='event'),
]
