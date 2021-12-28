from django.urls import path,re_path
from .views import *
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('home/',admin_home_view),
    path('candidates/',admin_candidates_view),
    path('companies/',admin_companies_view),
    path('companies/<int:account_id>',admins_companies_jobs_view),
    path('companies/<int:account_id>/<int:job_id>/',admins_applications_view),
    ]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)