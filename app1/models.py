from django.db import models
from django.contrib.auth.models import AbstractUser
from . managers import CustomUserManager


class CustomUser(AbstractUser):

    username = None
    email = models.EmailField(max_length = 100,unique = True)
    phone_no = models.CharField(max_length = 20)
    name = models.CharField(max_length = 20)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()



Role_Choice = (
    ('HR_Manager','HR Manager'),
    ('Junior HR','Junior HR'),
    ('Senior HR','Senior HR'),
    ('Senior Manage','Senior Manager'),
    ('Project manager','Project manager'),
    ('Team Leader','Team Leader'),
    ('Software Developer','Software Developer'),
    ('Web developer','Web developer'),
    ('App Developer','App Developer'),
    ('Intern/Trainee','Intern/Trainee')
)

Department = (
    ('Python','Python'),
    ('React','React'),
    ('Php','Php'),
    ('IOS','IOS'),
    ('Flutter','flutter'),
    ('HR','HR')
)

Experience = (
    ('0 - Year','0 - Year'),
    ('0-6 Month','0-6 Month'),
    ('1-2 Year','1-2 Year'),
    ('2-3 Year','2-3 Year'),

)

class EmployeeTable(models.Model):

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    username = models.CharField(max_length=20,unique=True)
    email = models.EmailField()
    phone_no = models.IntegerField()
    address = models.CharField(max_length=200)
    date_of_birth = models.DateField()
    Department = models.CharField(max_length=100,choices=Department)
    employee_role = models.CharField(max_length=100,choices=Role_Choice)
    experience = models.CharField(max_length=100,choices=Experience)
    password = models.CharField(max_length=20)
    token = models.CharField(max_length=500)

    def __str__(self):
        return self.username


class LeaveType_with_LeaveBalance(models.Model):

    Custom_Festival_Leave = models.FloatField(null=True,default=10)
    Leave_Without_Pay = models.IntegerField(null=True,default=10)   
    Privilege_Leave = models.IntegerField(null=True,default=10)
    Bereavement_Leave = models.IntegerField(null=True,default=10)
    username =  models.CharField(max_length=20,unique=True,null=True)


class Attendance(models.Model):

    username = models.CharField(max_length=20)
    email = models.EmailField(null=True)
    Department = models.CharField(max_length=20)
    check_in = models.DateTimeField(null=True)
    check_out = models.DateTimeField(null=True)





class Logtable(models.Model):
    
    date = models.DateField()
    email = models.EmailField()
    check_in = models.TimeField(null=True) 
    check_out = models.TimeField(null=True)
    total_hour = models.TimeField(null =True)  


class multiple_log(models.Model):

    date = models.DateField()
    email = models.EmailField()
    check_in = models.TimeField(null=True) 
    check_out = models.TimeField(null=True)



LeaveType = (
    ('Custom Festival Leave','Custom Festival Leave'),
    ('Leave Without Pay','Leave Without Pay'),
    ('Privilege Leave','Privilege Leave'),
    ('Bereavement Leave','Bereavement Leave'),
)

status_choice = (
    ('Accept','Accept'),
    ('Reject','Reject'),
    ('Pending','Pending')
)

leavechoice = (
    ('first half','first half'),
    ('second half','second half'),
    ('full day','full day')
)
class Leave_Request(models.Model):

    name = models.CharField(max_length=30)
    email  = models.EmailField(null=True)
    from_date = models.DateField(null=True)
    to_date = models.DateField(null=True)
    reason = models.CharField(null=True,max_length=200)
    leave_type = models.CharField(null=True,max_length=100,choices=LeaveType)
    total_days = models.CharField(null=True,max_length=20)
    status = models.CharField(null=True,max_length=100,default='Pending')
    selectleave = models.CharField(null=True,max_length=100,choices=leavechoice)

gender_choice = (
    ('M','Male'),
    ('F','Female'),
    ('O','Other')
)

developing_language = (
    ('Python','Python'),
    ('React','React'),
    ('Php','Php'),
    ('IOS','IOS'),
    ('Flutter','flutter'),
    ('HR','HR')
)

experience_in_field = (
    ('Fresher','Fresher'),
    ('6 Month','6 Month'),
    ('1 Year','1 Year'),
    ('2 Year','2 Year'),
    ('More than 2 year','More than 2 year')
)

Role_Choice = (
    ('HR_Manager','HR Manager'),
    ('Junior HR','Junior HR'),
    ('Senior HR','Senior HR'),
    ('Senior Manage','Senior Manager'),
    ('Project manager','Project manager'),
    ('Team Leader','Team Leader'),
    ('Software Developer','Software Developer'),
    ('Web developer','Web developer'),
    ('App Developer','App Developer'),
    ('Intern/Trainee','Intern/Trainee')
)

class RecruitmentSystem(models.Model):

    name = models.CharField(null=True,max_length=100)
    email = models.EmailField(null=True,unique=True)
    phone_no = models.PositiveIntegerField(null=True)
    age = models.PositiveIntegerField(null=True)
    gender = models.CharField(null=True,choices=gender_choice,max_length=10)
    # degree = models.CharField(null=True)
    applying_for = models.CharField(null=True,choices=developing_language,max_length=100)
    experience = models.CharField(null=True,choices=experience_in_field,max_length=100)
    resume = models.FileField(null=True)

    def __str__(self):
        return self.email

interview_status = (
    ('pending','pending'),
    ('under review','under review'),
    ('cleared','cleared'),
    ('rejected','rejected')
)

interview_round = (
    ('round-1','round-1'),
    ('round-2','round-2'),
    ('round-3','round-3')
)

class interview(models.Model):

    job_applicant = models.ForeignKey(RecruitmentSystem,to_field='email',on_delete=models.CASCADE,null=True)
    interviewRound = models.CharField(null=True,max_length=10,choices=interview_round)
    designation = models.CharField(null=True,choices=Role_Choice,max_length=30)
    scheduledTime = models.DateField(null=True)
    from_time = models.TimeField(null=True)
    to_time = models.TimeField(null=True)
    status = models.CharField(null=True,choices=interview_status,max_length=20)