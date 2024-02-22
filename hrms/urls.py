"""hrms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('emp_details/',views.EmployeeView),
    path('emp_update/<int:id>/',views.update),
    path('delete/<int:id>/',views.delete),
    path('emp_attendance/',views.emp_attendance),
    path('login/',views.emp_login),
    path('logout/',views.emp_logout),
    path('perm/',views.permission_by_email),
    path('permissionError/',views.permission_error),
    path('loginError/',views.login_error),
    path('group_permission/',views.group_permission),
    path('empCheckinlog/',views.employee_checkin_log),
    path('empCheckoutlog/',views.employee_checkout_log),
    path('multiplelog/',views.mutlipleLog),
    path('multiple_logout/',views.multipleLogOut),
    path('leave/',views.leave_apply),
    path('swan/',views.swan),
    path('accept/',views.werty),
    path('recurit/',views.recuritment),
    path('interview/',views.candidate_interview),
    path('interviewstatus/',views.interviewStatus)
]
