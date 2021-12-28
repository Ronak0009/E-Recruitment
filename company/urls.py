from django.urls import path,re_path
from .views import *
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('home/',home_view),
    path('new-job/',create_job_view),
    path('guni/new-job/',create_job_view),
    # path('interest/',interest_view),
    path('recruitment/',recruitment_view),
    path('recruitment/guni',recruitment_view),
    path('profile/',profile_view),
    path('guni/',home_view),

    path('complete-profile/company-profile/',complete_profile_view),
    path('edit-update-job/',edit_update_job_view),
    path('guni/edit-update-job/',edit_update_job_view),
    path('edit-update-job/<int:job_id>',company_job_edit_view),

    path('applications/',applications_view), 
    path('applications/<int:job_id>',company_schedule_view),

    path('applications/guni',guni_applications_view),   
 
    re_path(r'^job-applications/(?P<company_code>[0-9]{10})/(?P<job_id>[0-9]{10})/$',all_applications_view),
    re_path(r'^job-applications/export-excel/(?P<job_id>[0-9]{10})/$',export_excel_view),

    path('recruitment/<int:job_id>',create_quiz_view),
    path('recruitment/question/<int:job_id>',create_question_view),
    path('recruitment/question/<int:job_id>/<int:question_num>/',create_option_view),
    path('recruitment/result/<int:job_id>/<int:score>',company_result_view),
    re_path(r'^recruitment/result/(?P<job_id>[0-9]{10})/(?P<score>[0-9]{2})/export-excel/$',export_result_excel_view),
    path('recruitment/result/<int:job_id>/online-schedule',online_schedule_view),
    path('applications/<int:job_id>/online-schedule',online_schedule_view),

    re_path(r'^recruitment/result/(?P<job_id>[0-9]{10})/(?P<score>[0-9]{2})/process$',online_schedule_process_view),
    re_path(r'^recruitment/result/(?P<job_id>[0-9]{10})/selected-process$',selected_candidates_process),

    path('recruitment/result/<int:job_id>/upload-selected',upload_selected_candidates),
    path('recruitment/result/<int:job_id>/selected',candidates_selected_view),











    # path('complete-profile/education/',education_profile_view),
    # path('complete-profile/education/ssc',ssc_profile_view),
    # path('complete-profile/education/hsc',hsc_profile_view),
    # path('complete-profile/education/graduation',graduation_profile_view),
    # path('complete-profile/education/experience',experience_profile_view),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
