from django.shortcuts import render
from django.http import HttpResponse
from .admin import username,password
from .models import Employee
from .forms import EmployeeForm

# Create your views here.
def addEmployees(request):
    x=Employee.objects.get
    form= EmployeeForm(request.POST or None)
    if form.is_valid():
        form.save()
        form= EmployeeForm()
    context={ 
        'form':form,
    }
    #HttpResponse("Employee added Successfully")
    # thanks()
    return render (request, "details.html",context)

def displayEmployees(request):
    employees=Employee.objects.all()
    params={
        'employee':employees,
    }
    return render(request,'display.html',params)

def choice(request):
    user=request.POST.get('username','default')
    passw=request.POST.get('password','default')
    if user==username:
        if passw==password:
            return render(request,'choice.html')
        else:
            return HttpResponse('''<h1>Wrong Password</h1>
                                <a href="javascript:history.back()"><input type="button" value="Retry"></a>''')
    else:
         return HttpResponse('''<h1>Wrong Username</h1>
                             <a href="javascript:history.back()"><input type="button" value="Retry"></a>''')    
    
def updateEmployees(request):
    return render (request,'update.html')

def updatedEmployee(request):
    user=request.POST.get('updateUser','default')

    email=request.POST.get('newEmail','default')
    phone=request.POST.get('newPhone','default')
    dept=request.POST.get('newDepartment','default')
    role=request.POST.get('newRole','default')
    salary=float(request.POST.get('newSalary','default'))
    leaves=int(request.POST.get('newLeaves','0'))
    status=request.POST.get('newStatus','default')

    employee=Employee.objects.get(username=user)

    # l = leaves - 14
    if leaves > 0:
        salary=round(salary-(leaves*salary)/22,2)

    employee.email=email
    employee.phoneNumber=phone
    employee.department=dept
    employee.role=role
    employee.salary= salary
    employee.leaves=leaves
    employee.status=status
    employee.save()
    return HttpResponse('''<h1 style="text-align: center;">Employee details updated successfully.</h1>
                        <a href="../../display/"> <input type="button" name="btn" value="Display"></a>
                        <a href="javascript:history.back()"><input type="button" value="Retry"></a>''')

def deleteEmployees(request):
     return render (request,'delete.html')

def deletedEmployee(request):
    user=request.POST.get('delUser','default')
    x=Employee.objects.all()
    for i in x:
        if user==i.username:
            i.delete()
            return HttpResponse(f'''<h1 style="text-align: center;">Employee with username {user} deleted successfully.</h1>
                                <a href="../../display/" > <input type="button" name="btn" value="Display" C></a>
                                <br>
                                <br>
                                <a href="javascript:history.back()" ><input type="button" value="Back" style="margin-left: 50%;"></a>''')
    else:
        return HttpResponse('''<h1 style="text-align: center;">Username does not exist!</h1>
                            <a href="javascript:history.back()"><input type="button" value="Back" style="margin-left: 50%;"></a>''')

def login(request):
    return render(request,'index.html')