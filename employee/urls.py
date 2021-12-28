from django.urls import path,re_path
from .views import *
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    path('home/',home_view),
    path('applications/',interest_view),
    path('recruitment/',recruitment_view),
    path('profile/',profile_view),
    path('complete-profile/personal/',complete_profile_view),
    path('complete-profile/education/',education_profile_view),
    path('complete-profile/education/ssc',ssc_profile_view),
    path('complete-profile/education/hsc',hsc_profile_view),
    path('complete-profile/education/graduation',graduation_profile_view),
    path('complete-profile/education/experience',experience_profile_view),
    path('complete-profile/other/',other_profile_view),
    path('complete-profile/other/social',social_profile_view),
    re_path(r'^job-application/(?P<company_code>[0-9]{10})/(?P<job_id>[0-9]{10})/$',job_application_view),
    re_path(r'^applications/schedule-view/(?P<job>[0-9]{10})/$',candidate_schedule_view),
    # re_path(r'^quiz/(?P<job>[0-9]{10})/$',candidate_quiz_view),
    re_path(r'^recruitment/quiz/(?P<job>[0-9]{10})/$',candidate_quiz_view),
    re_path(r'^recruitment/quiz/(?P<job>[0-9]{10})/(?P<time>[0-9]{1})/(?P<name>.*)$',quiz_start),
    path('applications/result/<int:job_id>',candidates_result_view),




]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
