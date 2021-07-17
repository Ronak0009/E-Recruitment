from django.urls import path,re_path
from .views import *
from django.contrib import admin



urlpatterns = [
    path('home/',home_view),
    path('interest/',interest_view),
    path('recruitment/',recruitment_view),
    path('profile/',profile_view),
]