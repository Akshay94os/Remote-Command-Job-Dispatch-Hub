from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='job_home'),
    path('run/<int:pk>/', views.execute_job, name='execute_job'),
]
