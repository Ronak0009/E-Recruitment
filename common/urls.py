from django.urls import path,re_path, include
from .views import *
from django.contrib import admin
from django_email_verification import urls as mail_urls



urlpatterns = [
    path('',redirect_to_dashboard),
    path('main-dashboard/',main_dashboard),
    # path('registration/<int:no>',registration_view),
    # path('login/<int:no>',login_view, name='login'),
    path('login/<int:no>',login_process_view),
    path('vchat/',video_chat),
    path('logout/',logout_view),
    path('registration/2',company_registration),
    path('registration/1',candidate_registration),
    path('not-verified/',not_verified),
    path('pending-account/',pending_view),
    path('email/', include(mail_urls)),

]