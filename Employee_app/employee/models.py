from django.db import models

# Create your models here.
class Employee_position(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Employee(models.Model):
    fullname = models.CharField(max_length=100)
    emp_code = models.CharField(max_length=10)
    mobile = models.CharField(max_length=20)
    postion = models.ForeignKey(Employee_position, models.DO_NOTHING)

    def __str__(self):
        return f"Employee {self.id} is {self.fullname}"

