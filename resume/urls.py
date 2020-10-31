from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('projects/', views.project_list),
    path('projects/<int:pk>', views.project_detail),
    path('resume/', views.resume_list),
]