from django.shortcuts import render
from .models import User
from enroll.forms import student
from django.http import HttpResponseRedirect
# Create your views here.
def home(request):
    if request.method =="POST":
        fm =student(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            pw=fm.cleaned_data['password']
            rpw=fm.cleaned_data['repassword']
            reg=User(name=nm,email=em,password=pw,repassword=rpw)
            reg.save()
            fm=student()
            
            # return HttpResponseRedirect('/')
        # else:
        #     return HttpResponseRedirect(/) 
    else:
        fm=student()
    stud=User.objects.all()
    return render(request,'enroll/home.html',{'form':fm,'stu':stud})

