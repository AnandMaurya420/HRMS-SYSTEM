from django.contrib import admin
from .models import CustomUser,EmployeeTable,Attendance,Logtable,multiple_log,Leave_Request,LeaveType_with_LeaveBalance,RecruitmentSystem,interview

# Register your models here.

@admin.register(CustomUser)
class customUserAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'email', 'phone_no', 'password']

@admin.register(EmployeeTable)
class Employee_data(admin.ModelAdmin):

    list_display = ['id','first_name','last_name','username','email','phone_no','date_of_birth','address','employee_role','Department','experience','password']

@admin.register(Attendance)
class Attendance_table(admin.ModelAdmin):

    list_display = ['id','username','email','Department','check_in','check_out']

# @admin.register(EmployeeLog)

# class employeelog_table(admin.ModelAdmin):
    
#     list_display = ['id','username','email','Department','check_in','check_out','total_hour']

@admin.register(Logtable)
class EmployeeLogTable(admin.ModelAdmin):

    list_display = ['id','date','email','check_in','check_out','total_hour']

@admin.register(multiple_log)
class EmployeeLogTable(admin.ModelAdmin):

    list_display = ['id','date','email','check_in','check_out']


@admin.register(Leave_Request)
class Leave_table(admin.ModelAdmin):

    list_display = ['id','name','email','from_date','to_date','reason','leave_type','total_days','status','selectleave']


@admin.register(LeaveType_with_LeaveBalance)
class LeaveType_and_LeaveBalance(admin.ModelAdmin):

    list_display = ['id','Custom_Festival_Leave','Leave_Without_Pay','Privilege_Leave','Bereavement_Leave','username']

@admin.register(RecruitmentSystem)
class recuritment(admin.ModelAdmin):

    list_display = ['id','name','email','phone_no','age','gender','applying_for','experience','resume']

@admin.register(interview)
class interview(admin.ModelAdmin):

    list_display = ['id','job_applicant','interviewRound','designation','scheduledTime','from_time','to_time','status']


