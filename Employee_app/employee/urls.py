from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.employee_form, name= "employee_form"),
    path('employee_list/', views.employee_list, name ="employee_list"),
    path('<int:id>/',views.employee_form, name = "update_form" ),
    path('delete_emp/<int:empid>',views.delete_emp, name = "delete_form" ),
    path('addposition/', views.addposition, name= "addposition")
]