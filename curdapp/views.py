from django.shortcuts import render,redirect
from .models import EmpData

def homepage(request):
    emps=EmpData.objects.all()
    return render(request,'homepage.html',{'emps':emps})

def addingEmp(request):
    if request.method=="GET":
        return render(request,'addingEmp.html')
    else:
        EmpData(
        first_name=request.POST['fname'],
        last_name=request.POST['lname'],
        email=request.POST['email'],
        mobile=request.POST['mobile'],
        company=request.POST['company'],
        salary=request.POST['salary'],
        location=request.POST['location'],

        ).save()
        return redirect(homepage)
def updatingEmp(request, id):
    emp=EmpData.objects.get(id=id)
    return render (request, 'updatingEmp.html', {'emp':emp})

def updating_Emp(request, id):
    emp=EmpData.objects.get(id=id)
    emp.first_name=request.POST['fname']
    emp.last_name=request.POST['lname']
    emp.email=request.POST['email']
    emp.mobile=request.POST['mobile']
    emp.company=request.POST['company']
    emp.salary=request.POST['salary']
    emp.location=request.POST['location']
    emp.save()
    return redirect(homepage)

def delete(request, id):
    emp=EmpData.objects.get(id=id)
    emp.delete()
    return redirect(homepage)
