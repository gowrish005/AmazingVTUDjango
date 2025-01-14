from django.urls import path

from amazingvtu import settings
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.main_page, name='main'),
    path('branches/<int:semester_id>/', views.branch_page, name='branches'),  # updated 'semester_id' to 'semester'
    path('subjects/<int:branch_id>/', views.subject_page, name='subjects'),
    path('modules/<int:subject_id>/', views.modules_page, name='modules'),
    path('defualt', views.defualt, name='defualt'),  # fix typo from 'defualt' to 'default'
    path('admins/uploads/', views.upload_module, name='admin_uploads'),
    path('admins/create-branch/', views.create_branch, name='create_branch'),
    path('create-branch/', views.create_branch, name='create_branch'),
    path('create-subject/', views.create_subject, name='create_subject'),
    path('get-branches/<int:semester_id>/', views.get_branches, name='get_branches'),
    path('get-subjects/<int:branch_id>/', views.get_subjects, name='get_subjects'),
]
if not settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)