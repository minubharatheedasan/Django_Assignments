from .models import Employee, Employee_position
from django.shortcuts import redirect, render
from .forms import EmployeeForm

# Create your views here.


def employee_form(request, id=0):
    if request.method == 'GET':
        if id == 0:
            form = EmployeeForm()
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(instance = employee)
        return render(request, "employee/Employee_form.html",{'form':form})
    else:
        if id == 0: 
            form_1 = EmployeeForm(request.POST)
        else:
            employee = Employee.objects.get(pk=id)
            form_1 = EmployeeForm(request.POST, instance=employee)
        if form_1.is_valid():
            form_1.save()
        return redirect('/employee/employee_list/')

def employee_list(request):
    context = {'employee_list':Employee.objects.all()}
    return render(request, 'employee/Employee_list.html', context)

def delete_emp(request,empid):
    if request.method == "GET":
        del_emp = Employee.objects.filter(pk=empid)
        del_emp.delete()
    return redirect('/employee/employee_list/')

def addposition(request):
    #print(request.method)
    if request.method == "POST":
        title_1 = request.POST.get("title")
        print("Title1",title_1)
        obj = Employee_position(title =title_1)
        obj.save()
        # #pos = Employee_position.objects.get('title')    
        # form2  = EmployeeFormpos(request.POST)
        # if form2.is_valid():
        #     form2.save()
    return redirect('/employee/employee_list/')