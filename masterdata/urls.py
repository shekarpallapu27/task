from .views import *
from django.conf.urls import url

urlpatterns = [

    url(r'^$', index),
    url(r'dashboard/$', dashboard),
    # url(r'login/$', login),
    # url(r'^login/$', login_call),
    # url(r'^dashboard/$', dashboard, name='dashboard'),
    # url(r'dashboard/$', home),


    url(r'^logout/$', user_logout, name='logout'),


    url(r'api/class/(?P<cls_name>.*)/$', ClassDetails.as_view()),
    url(r'api/student/(?P<student_name>.*)/$', StudentDetails.as_view()),
    url(r'api/year/(?P<year>.*)/$', YearDetails.as_view()),
   
    url(r'class_data/$', cls_data),
    url(r'student_data/$', std_data),
    url(r'year_data/$', yrs_data),
    ]