from django.contrib import admin

# Register your models here.
from .models import Employee, Employee_position

admin.site.register(Employee)
admin.site.register(Employee_position)
