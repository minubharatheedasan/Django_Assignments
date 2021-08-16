from django import forms
from .models import Employee
from .models import Employee_position


class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = ('fullname', 'emp_code', 'mobile', 'postion')
        labels = {
            'fullname' : 'Full Name',
            'emp_code' : 'Emp. Code'
        }
       

    def __init__(self, *args, **kwargs):
        super(EmployeeForm,self).__init__(*args, **kwargs)
        self.fields['postion'].empty_label = "select"

# class EmployeeFormpos(forms.ModelForm):
#     class Meta:
#         model = Employee_position
#         fields = ('title',)
#         labels = {
#         'title' : 'Employee Position'
#         }