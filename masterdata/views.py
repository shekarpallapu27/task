from django.shortcuts import render

# Create your views here.


from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from django.http import HttpResponse,JsonResponse
from django.shortcuts import redirect
from django.contrib import auth
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required


def index(request):
    if request.method=="GET":
        if request.user.is_authenticated():
            return HttpResponseRedirect('/dashboard/')
        return render(request,'index.html')
    else:
        username = request.POST.get('uname', '')
        password = request.POST.get('psw', '')
        user = auth.authenticate(username = username, password = password)
        device_ip = Login.objects.get(user__pk=user.id).allowed_ip
        request_ip = request.META['REMOTE_ADDR']
        if user is not None and device_ip==request_ip:
            auth.login(request, user)
            return HttpResponseRedirect('/dashboard/')
        else:
            return render(request,'index.html')


@login_required
def user_logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')




@login_required(login_url="/")
def dashboard(request):
    return render(request,'dashborad.html')


class ClassDetails(APIView):
    
    def get(self, request,cls_name):
        report_obj = ReportDetails.objects.filter(std=cls_name)
        obj = ReportSerializer(report_obj,many=True)
        # import ipdb;ipdb.set_trace()
        return Response(obj.data)


class StudentDetails(APIView):
    
    def get(self, request,student_name):
        report_obj = ReportDetails.objects.filter(student__student_name=student_name)
        obj = ReportSerializer(report_obj,many=True)
        
        return Response(obj.data)


class YearDetails(APIView):
    
    def get(self, request,year):
        report_obj = ReportDetails.objects.filter(Year=year)
        obj = ReportSerializer(report_obj,many=True)
        return Response(obj.data)


def cls_data(request):
    # import ipdb;ipdb.set_trace()
    # cls_obj = ReportDetails.objects.all().values('std')
    cls_obj=list(set(ReportDetails.objects.all().values_list('std',flat=True)))
    return JsonResponse({'data':cls_obj})

def std_data(request):
    # import ipdb;ipdb.set_trace()
    std_obj = list(set(IdMapping.objects.all().values_list('student_name',flat=True)))
    return JsonResponse({'data':std_obj})

def yrs_data(request):
    # year_obj = ReportDetails.objects.all().values('Year')
    year_obj=list(set(ReportDetails.objects.all().values_list('Year',flat=True)))
    return JsonResponse({'data':year_obj})
