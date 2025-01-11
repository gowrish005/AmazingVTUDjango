# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main'),
    path('branches/<int:year_id>/', views.branch_page, name='branches'),
    path('subjects/<int:branch_id>/', views.subject_page, name='subjects'),
    path('modules/<int:subject_id>/', views.modules_page, name='modules'),
    path('defualt', views.defualt, name='defualt'),
]
