from django.urls import path,re_path
from .views import *
from django.contrib import admin



urlpatterns = [
    path('main-dashboard/',main_dashboard),
    path('registration/<int:no>',registration_view),
    path('login/<int:no>',login_view),

]