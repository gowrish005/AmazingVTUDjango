from django.urls import path

from amazingvtu import settings
from . import views
from django.conf.urls.static import static

urlpatterns = [
    # Main page
    path('', views.main_page, name='main'),

    # Branches and subjects
    path('branches/<int:semester_id>/', views.branch_page, name='branches'),
    path('subjects/<int:branch_id>/', views.subject_page, name='subjects'),
    path('modules/<int:subject_id>/', views.modules_page, name='modules'),

    # Admin functionalities
    path('admins/uploads/', views.upload_module, name='admin_uploads'),
    path('admins/create-branch/', views.create_branch, name='create_branch'),
    path('admins/control-panel/', views.admin_control_panel, name='admin_control_panel'),

    # Creation functionalities
    path('create-branch/', views.create_branch, name='create_branch'),
    path('create-subject/', views.create_subject, name='create_subject'),

    # Get branches and subjects
    path('get-branches/<int:semester_id>/', views.get_branches, name='get_branches'),
    path('get-subjects/<int:branch_id>/', views.get_subjects, name='get_subjects'),

    # Default page
    path('default', views.defualt, name='default'),  # fixed typo from 'defualt' to 'default'
]
if not settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)