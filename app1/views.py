from django.shortcuts import render
from . models import EmployeeTable,CustomUser,Attendance,Logtable,multiple_log,Leave_Request,LeaveType_with_LeaveBalance,RecruitmentSystem,interview
from django.views.decorators.csrf import csrf_exempt
import jwt
from django.http import JsonResponse
# from django.contrib.auth import logout,authenticate,login as login_user
from django.contrib.auth import logout,authenticate,login
import datetime

from datetime import timedelta
import time
from datetime import datetime,date 
from django.utils import timezone
import dateutil.parser
from django.utils.dateparse import parse_datetime
import dateutil.parser
from django.contrib.auth.decorators import permission_required,login_required
from django.contrib.auth.models import  Permission, Group
from django.contrib.contenttypes.models import ContentType



# Create your views here.
@csrf_exempt
# @login_required(login_url='/loginError/')
# @permission_required('app1.add_employeetable',login_url='/permissionError/')
def EmployeeView(request):
    
    if request.method == 'POST':
        # emp_logout_log(request)
        print("================================")
        first_name = request.POST.get('first_name')
        last_name = request. POST.get('last_name')
        email = request.POST.get('email')
        phone_no = request.POST.get('phone_no')
        address = request.POST.get('address')
        date_of_birth = request.POST.get('date_of_birth')
        employee_role = request.POST.get('employee_role')
        Department = request.POST.get('Department')
        experience = request.POST.get('experience')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        username = request.POST.get('username')
        
        data = EmployeeTable.objects.filter(email = email)
        if data:
            print('==user already register===',data)
            return(JsonResponse({'data':'user already register'}))
    
        else:

            if password == confirm_password:
                    print('00000000000000000')
                    encoded_jwt = jwt.encode({'email': email,'password':password}, 'secret', algorithm='HS256')
                    print('encoded',encoded_jwt )
                    data = EmployeeTable.objects.create(token=encoded_jwt,first_name=first_name,last_name=last_name,username=username,email=email,phone_no=phone_no,address=address,date_of_birth=date_of_birth,employee_role=employee_role,Department=Department,experience=experience,password=password)
                    data.save()
                    user = CustomUser.objects.create(name=username,email=email,phone_no = phone_no,password=password    )
                    user.set_password(password) 
                    user.save()

                    dwr = LeaveType_with_LeaveBalance.objects.create(username=username)
                    dwr.save()
                    print('====>',data)
                    return JsonResponse({'data': 'data add sucessfully'})
            else :
                return JsonResponse({'data':'password not match'})
    else:
        return(JsonResponse({"data":'from the get side'}))



# @login_required(login_url='/loginError/')
# @permission_required('app1.change_employeetable',login_url='/permissionError/')
@csrf_exempt
def update(request,id):   
    if request.method == 'POST':
        print("=========================")
        # emp_logout_log(request)
        data = EmployeeTable.objects.get(id=id)
        userdata = CustomUser.objects.get(id=id)
        # data.first_name = request.POST.get('first_name')
        # data.first_name = request.POST.get('first_name')
        # data.last_name = request.POST.get('last_name')
        # data.address = request.POST.get('address')
        # data.email = request.POST.get('email')
        # data.phone_no = request.POST.get('phone_no')
        # userdata.phone_no = data.phone_no
        # data.designation = request.POST.get('designation')
        # data.department = request.POST.get('department')
        data.employee_role = request.POST.get('employee_role')
        # data.password = request.POST.get('password')
        # confirm_password = request.POST.get('confirm_password')
        data.save()
        userdata.save()

        return JsonResponse({'data': 'user update sucessfully'})
            # user.save()
    else:
        return JsonResponse({'data':'user not found'})


@login_required(login_url='/loginError/')
@permission_required('app1.add_employeetable',login_url='/permissionError/')
@csrf_exempt
def delete(request,id):

    try:
        data = EmployeeTable.objects.get(pk=id)
        data.delete()
        return JsonResponse({"data":'data deleted sucessfully'})
    except:
        return JsonResponse({'data':'id not found'})

@csrf_exempt
def emp_login(request):

    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password'] 

        try:
            data = EmployeeTable.objects.get(email=email)
            user = authenticate(request, email=email, password=password)

            if user is not None:

                old_token = EmployeeTable.objects.get(email=email)
                print('old_token',type(old_token.token),old_token.token)

                new_token = jwt.encode({'email': email,'password':password}, 'secret', algorithm='HS256')
                print('==token===>',type(str(new_token)),new_token) 

                if str(new_token) == old_token.token:
                    print("<==================>")
                    login(request, user)
                    print("======login=====",request.user)
                    # emp_attendance(request) 
                    # employee_checkin_log(request)  
                    # mutlipleLog(request)

                    return JsonResponse({'data':'user login sucessfully'})       
                else:
                    return JsonResponse({'data':'user not found'})
            else:
                print("======please fill the form =======")
        except:
            print("======user not found =================")
            return JsonResponse({'data':'===user not found '})
            
    else:
        print("====== request not from the get =======")

# @login_required(login_url='/loginError/')
@csrf_exempt
def emp_logout(request):

    if request.method == 'POST':

        # # if request.user:
        #     loger_email = request.user
        #     print("====loger_email===",loger_email)

            loger_email = request.user
            print("========logeremail========",loger_email)
            current_time = datetime.datetime.now()
            formatted_datetime = parse_datetime(str(current_time)).strftime('%Y-%m-%d %H:%M:%S')

            try:
                check_in_time  = []
                log_out_attendance = Attendance.objects.all().filter(email = request.user)
                print("=======logoutatt=======",log_out_attendance)

                for i in log_out_attendance:
                    usercheckin = i.check_in
                    check_in_time.append(usercheckin)
                    print("=======useremail======",usercheckin)

                print("=======log_out_attendance===",log_out_attendance)

                b = check_in_time[-1].date()
                print("========b========",b)
                current_date = datetime.datetime.now().date()
                print("=======current_date======",current_date)

                request_data = request.user
                if b == current_date:
                # if log_out_attendance:
                    print("==============")
                    for i in log_out_attendance:
                        print("======i======",i.check_in)   

                    i.check_out = formatted_datetime
                    i.save()
                    logout(request)
                    print("========function fault=============")
                    employee_checkout_log(request_data)
                    # multipleLogOut(request_data)
                    
                    print('=======log_out_log========>')
                    return JsonResponse({'data':'logout sucessfully'})
                else:
                    return JsonResponse({'data':'login_first'})
            except:
                print("=====login -first ==============")
                return JsonResponse({'data':'except_login_first'})
        # else:
            # return JsonResponse({'data':'login_first'})
    else:
        return JsonResponse({'data':'request not from post side'})


@csrf_exempt
def emp_attendance(request):

        # if request.user:
        
            try:
                print("===typeof=======",type(request.user))
                emp = EmployeeTable.objects.get(email=request.user)
                print("=====request.user==========",request.user)
                print("=====================",type(emp.email))

                if emp.email:
                    try:
                        print("=1=1=1=1==1=1=",request.user)
                        attendance_data = Attendance.objects.all().filter(email = emp.email)
                        checkin_data = []
                        print("=======if=====")
                        print("======= attendance_data=========",attendance_data)
                        for i in attendance_data:
                            print("==========check check ==========")
                            check = i.check_in
                            checkin_data.append(check)
                        print("==check===",type(checkin_data[-1]))
                        b = checkin_data[-1].date()
                        # d = dateutil.parser.parse(checkin_data[-1]).date()
                        print("=========date=========",b)
                        
                        current_date = datetime.datetime.now().date()
                        print("========print======================")
                        print("========currrent_time===========",current_date)

                        if checkin_data[-1].date() != current_date:
                            print("=======after_if=============")
                            print("=====empe emp emp emp========",emp)
                            # for i in emp:

                            print("=====print for =====")
                            attendance_user = emp.username
                            attendance_email = emp.email
                            attendance_department = emp.Department
                            print("===>",attendance_department)

                            today_time = datetime.datetime.now()      
                            print("========= today time=====",today_time)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
                            # print("======current_time======",current_time.time())

                            # posted = timezone.now()
                            # print("=======posted=========",posted)
                            # checkinTime = time.localtime()

                            parser_date = dateutil.parser.parse(str(today_time))
                            print("======parser_date======",parser_date,type(parser_date))

                            formatted_datetime = parse_datetime(str(today_time)).strftime('%Y-%m-%d %H:%M:%S')
                            print("=======formated-1 time======",formatted_datetime)

                            attend = Attendance.objects.create(username=attendance_user,email = attendance_email,Department=attendance_department,check_in = formatted_datetime)
                            attend.save()
                            print("=====attendance save=========")
                        else:
                            print("==============already exist=====================")
                    except:

                        emp = EmployeeTable.objects.get(email=request.user)
                        print("=====request.user==========",request.user)
                        print("=====================",emp.email)
                        today_time = datetime.datetime.now()    
                        
                        # posted = timezone.now()
                        # print("=======posted=========",posted,type(posted))

                        # parser_date = dateutil.parser.parse(str(today_time))
                        # print("======parser_date======",parser_date,type(parser_date))

                        formatted_datetime = parse_datetime(str(today_time)).strftime('%Y-%m-%d %H:%M:%S')
                        print("=======formated time======",formatted_datetime)
                        print("=======formated time======",type(formatted_datetime))

                        attend = Attendance(username=emp.username,email = emp.email,Department=emp.Department,check_in=formatted_datetime)
                        attend.save()
                        print("=========================================================================")        
                else:
                    print("===data not in attendance table =====")
            except:
                print("==============except=======================")
                return JsonResponse({'data':'ecxceptionnnnnn'})


@csrf_exempt
def permission_by_email(request):

    content_type = ContentType.objects.get_for_model(EmployeeTable)
    print("====contenttype========",content_type)
    permission_list = ['add_employeetable','change_employeetable','view_employeetable','delete_employeetable']
    post_permission = Permission.objects.filter( content_type = content_type)
    print("======postpermission========",post_permission)

    for perm in post_permission:
        print("======perm======",perm)

        user = CustomUser.objects.get(email="abraar@gmail.com")
        print("==user===",user)
        user.user_permissions.add(perm)
        print("====permission_added=====")
        print(user.has_perm("app1.view_EmployeeTable"))

    return JsonResponse({'data':'permission got it'})

def permission_error(request):
    return JsonResponse({'data':'you have no permission'})

def login_error(request):
    return JsonResponse({'data':'please login first'})

@csrf_exempt
def group_permission(request):

    if request.method == "POST":
        author_group, created = Group.objects.get_or_create(name="HR Department")

        content_type = ContentType.objects.get_for_model(EmployeeTable)
        post_permission = Permission.objects.filter(content_type=content_type)

        for perm in post_permission:
            print("=====after for ;oop ====")
            author_group.permissions.add(perm)
            print("=====after ====")
            # user = EmployeeTable.objects.all().filter(Department = "HR")
            # for i in user:
            #     b = i.Department
            #     print("-=====use===",b)
            # user.Department.user_permissions.add(perm)
            print("==================================================")
        # print("===cg====",user)   

# =========== code for assign a user in group =====================
        user = CustomUser.objects.get(email = "shweta@gmail.com")
        user.groups.add(author_group)

@csrf_exempt
def employee_checkin_log(request):

    if request.method == 'POST':

        email = request.user
        print("=====typeof=====",type(str(email)),email)
        current_time = datetime.datetime.now().time()
        current_date = datetime.datetime.now().date()
        print("=====currenttime =========",current_time)

        try:
            print("========try============")
            emp_checkInLog = Logtable.objects.all().filter(email = email)
            checklog = []

            for i in emp_checkInLog:
                checdate = i.date
                checout = i.check_out
                checklog.append(checdate)
            print("==============")

            print("=====empcheckinlog========",emp_checkInLog)
            print("=======checklog[-1]=====",checklog[-1])
            # print("=================0==============",checout)

        # try:
            if current_date == checklog[-1]  and checout != None:
                print("=================00==============")
                emplog = Logtable.objects.create(date = current_date, email = str(email), check_in = current_time)
                emplog.save()
                print("=================1==============")

            elif current_date == checklog[-1] and checout == None:
                print("==========2============")
                pass

            elif current_date != checklog[-1]:
                
                print("============akash=============")
                emplog = Logtable.objects.create(date = current_date, email = str(email), check_in = current_time)
                emplog.save()
                print("============3============")
                # pass
            else:
                print("======= not a nullll=========")
            # except:
            #     print("==================except============")
        except:
            print("=================000==============")
            emplog = Logtable.objects.create(date = current_date, email = str(email), check_in = current_time)
            emplog.save()
    else:
        print("=====request not from post side =======")

@csrf_exempt
def employee_checkout_log(request):
       
    if request.method == 'POST':
        
        try:
            emplogtab = Logtable.objects.all().filter(email = request.user)
            print("=======logoutatt=======",emplogtab)
            current_time = datetime.datetime.now().time()
            current_date = datetime.datetime.now().date()

            for i in emplogtab:
                print("===========for===============")
                useremail = i.email
                print("======typeof======",type(useremail))
                usercheckout = i.check_out
                userDate = i.date
                print("=========usercheckout=======",usercheckout)

            if usercheckout == None and current_date == userDate:    
                i.check_out = current_time
                i.save()
                print("==========================save=============")
                return JsonResponse({'data':"logout_sucessfully"})
                # check_in_time.append(usercheckin)
                # print("=======useremail======",user/checkin)
            else:
                print("==== already checkout ====")
                return JsonResponse({'data':"already check_out"})
        except:
            return JsonResponse({'data':'data_not_found'})

@csrf_exempt
def mutlipleLog(request):

    if request.method == 'POST':
        email = request.user
        try:
            employee_table = multiple_log.objects.all().filter(email = request.user)
            print("=====typeof=====",type(str(email)))
            current_time = datetime.datetime.now().time()
            current_date = datetime.datetime.now().date()
            print("=====currenttime =========",current_time)
            emplog = multiple_log.objects.create(date= current_date, email = str(email), check_in = current_time)
            emplog.save()

            # email = request.user
            # emplogtab = multiple_log.objects.all().filter(email = request.user)
            # for i in emplogtab:
            #     useremail = i.email
            #     usercheckin = i.check_in
            #     usercheckout = i.check_out
            # emplog = mutlipleLog.objects.create(email = str(email), check_in = current_time)
        except:
            emplog = multiple_log.objects.create(date= current_date, email = str(email), check_in = current_time)
            emplog.save()
            print("=================================================")

        # for i in employee_table:

        #     checkIN = i.check_in
        #     checkOut = i.checkout
        #     userDate = i.date
        #     print("======i.email====",i.username)
        
        # if checkIN != None and checkOut == None and current_date == userDate:
        #     emplog = mutlipleLog.objects.create(date = current_date, email = str(email), check_in = current_time)
        #     emplog.save()
        
        # elif checkIN == None:
        #     emplog = mutlipleLog.objects.create(date = current_date, email = str(email), check_in = current_time)
        #     emplog.save()

@csrf_exempt
def multipleLogOut(request):

        if request.method == 'POST':

        # check_in_time  = []

            emplogtab = multiple_log.objects.all().filter(email = request.user)
            print("=======logoutatt=======",emplogtab)
            current_time = datetime.datetime.now().time()
            current_date = datetime.datetime.now().date()
            print("=======currenr_date=====",current_date)

            for i in emplogtab:
                print("===========for===============")
                useremail = i.email
                print("======typeof======",type(useremail))
                usercheckout = i.check_out
                print("=========usercheckout=======",usercheckout)

            print("=========usercheckout=======",usercheckout)
            if i.date == current_date and usercheckout == None:
                i.check_out = current_time
                i.save()
                print("==========================save=============")
            # check_in_time.append(usercheckin)
            # print("=======useremail======",user/checkin)

            elif i.check_out != None:
                
                print("========elif============")
                emplog = multiple_log.objects.create(date = current_date, email = str(request.user), check_out = current_time)
                emplog.save()
            else:
                print("======= already checkout ======")

# =============================   leave system start ==================================================

@csrf_exempt
def leave_apply(request):

    if request.method == 'POST':
       
        logger = request.user
        # print("=====logger ==========",logger)
        # obt = EmployeeTable.objects.all().filter(email = logger)
        obt = EmployeeTable.objects.get(email = logger)
        userName = obt.username

        from_date = request.POST.get('from_date')
        to_date = request.POST.get('to_date')
        reason = request.POST.get('reason')
        leave_type = request.POST.get('leave_type')

        start_date = datetime.strptime(from_date, "%Y-%m-%d").date()
        end_date = datetime.strptime(to_date, "%Y-%m-%d").date()
        print("==start_date ===",type(start_date))
        # mydata = EmployeeTable.objects.filter(username='akash').values()

        aw = LeaveType_with_LeaveBalance.objects.get(username=userName)
        # print('=======awawawawawaw=======',aw)
        # leavePerson = aw.username
        # print("=====aw=======",leavePerson)

        a = time.mktime(time.strptime(from_date, "%Y-%m-%d"))
        b = time.mktime(time.strptime(to_date, "%Y-%m-%d"))
        delta = b - a
        leave_days = delta/86400
        leaveDay = f"{int(leave_days)} days"
        # print("===11===11===")
        try:
            leaverequest = Leave_Request.objects.all().filter(email=logger)
            # print("===2===2==")
            # print("========leave======",leaverequest)

            if not leaverequest:
                # print("=======blank=======")
                if start_date <= end_date:
                        
                    if leave_type :
                        # print("=====2===2=2=2=2=2=2====")
                        # print("====awaw====",aw)
                        # print("=====leaveType===",leaveType)
                        ab = aw.Custom_Festival_Leave

                        # print("=====ababab=====>",ab)
                        remainingLeave = int(ab) - int(leave_days)
                        # print("=======try1=======")
                        if int(leave_days) <= int(ab) :

                            leaveRequest = Leave_Request.objects.create(name = userName, email = str(logger), from_date = from_date, to_date = to_date, reason = reason, leave_type = leave_type, total_days = leaveDay)
                            leaveRequest.save()
                            # print("==== try-leave =====")
                            # cd = EmployeeTable.objects.filter(email = logger,leave_balance_id =1).update(Custom_Festival_Leave=3)
                            aw.Custom_Festival_Leave = remainingLeave
                            aw.save()
                            
                            # print("========= leaveapply suessfully ============")
                            return JsonResponse({'data':"leaveapplyied suessfully"})
                        else:
                            print(f"<=====you have only{ab} days and you are applying {leaveDay}====>")
                    else:      
                        print("================== leave type cusomfestival ===================")
                else:
                    print(f"start date{start_date} must be greater than end date{end_date}")

            else:
                # print("=======first else=======")
                leaverequest = Leave_Request.objects.all().filter(email=logger)
                if end_date >= start_date:
                    # print("=======first else=======")
                    for i in leaverequest:
                        # print("=========iii=====",i.email)
                        # print("===sky====start_date else=======",start_date)
                        # print("===sky====start_date else=======",i.from_date,i.to_date)

                        if i.from_date <=start_date <= i.to_date:
                            return JsonResponse({'data':"leave already apply on this date"})

                        # if from_date in (fm_date,t_date) or to_date in (fm_date,t_date):
                            # print("==sky=====  you already applied leave on this day ======",start_date,end_date)
                        else:
                            print("===sky====elseeeee=======")
                            print("========>>>>>>>>>>.",leave_type)
                            if leave_type :
                                # print("=======first else=======")
                                ab = aw.Custom_Festival_Leave
                                # print("=====ab=====>",ab)
                                remainingLeave = int(ab) - int(leave_days)

                                if int(leave_days) <= int(ab) :

                                    leaveRequest = Leave_Request.objects.create(name = userName, email = str(logger), from_date = from_date, to_date = to_date, reason = reason, leave_type = leave_type, total_days = leaveDay)
                                    leaveRequest.save()
                                    # print("====leaveRequest=====")
                                    aw.Custom_Festival_Leave = remainingLeave
                                    aw.save()
                                    # print("======= --000000000000000000000-- ========")
                                    return JsonResponse({'data':'----- leave applied ------'})
                                else:
                                    print("==== you have no leave ====")
                                    return JsonResponse({'data':'---you have no leave'})
                            else:
                                print("=========else5============")
                else:
                    print("=======from date must be less than to date ==========")
                    return JsonResponse({'data':'---from date must be less than to date'}) 
        except:
            print("====except=====")
            if start_date <= end_date:
                        
                if leave_type :
                    ab = aw.Custom_Festival_Leave
                    print("=====ab-------",ab)
                    remainingLeave = int(ab) - int(leave_days)
                    print("========except1=======")
                    if int(leave_days) <= int(ab) :

                        leaveRequest = Leave_Request.objects.create(name = userName, email = str(logger), from_date = from_date, to_date = to_date, reason = reason, leave_type = leave_type, total_days = leaveDay)
                        leaveRequest.save()
                        print("==== except leaverequest =====")
                        aw.Custom_Festival_Leave = remainingLeave
                        aw.save()
                        
                        print("========= leaveapply suessfully ============")
                        return JsonResponse({'data':"leaveapplyied suessfully"})
                    else:
                        print(f"<=====you have only{ab} days and you are applying {leaveDay}====>")
                else:      
                    print("================== please enter leave type ===================")
            else:
                print(f"start date{start_date} must be less than end date{end_date}") 

    else:
        print("==========================other===============")

@csrf_exempt
def swan(request):

    if request.method == 'POST':
        logger = request.user
        obt = EmployeeTable.objects.get(email = logger)
        userName = obt.username

        from_date = request.POST.get('from_date')
        to_date = request.POST.get('to_date')
        reason = request.POST.get('reason')
        leave_type = request.POST.get('leave_type')
        selectleave = request.POST.get('selectleave')
        # status = request.POST.get('status')
        # notify = request.POST.get('notify')

        start_date = datetime.strptime(from_date, "%Y-%m-%d").date()
        end_date = datetime.strptime(to_date, "%Y-%m-%d").date()
        print("==start_date ===",type(start_date))

        a = time.mktime(time.strptime(from_date, "%Y-%m-%d"))
        b = time.mktime(time.strptime(to_date, "%Y-%m-%d"))

        delta = b - a
        leave_days = (delta/86400)+1
        print("=== type ====",leave_days,type(leave_days))
        leaveDay = f"{int(leave_days)} days"

        halfleave_day = (delta/86400) + 0.5
        print("==half-day----",type(halfleave_day))
        LeaveDay = f"{(halfleave_day)} days"
        print("====leaveday===",LeaveDay,type(LeaveDay))

        aw = LeaveType_with_LeaveBalance.objects.get(username=userName)

        
        if start_date <= end_date:
            if leave_type:
                ab = aw.Custom_Festival_Leave
                print("==ab==",type(ab))
                remainingLeave = (ab) - int(leave_days)
                Remainigleave = (ab) - (halfleave_day)
                print("==leave_type-1==",Remainigleave,type(Remainigleave))
                
                try:
                    print("==try====")
                    leaverequest = Leave_Request.objects.all().filter(email=logger)
                    if not leaverequest:
                        
                        if selectleave == 'first half' or 'second half':
                            leaveRequest = Leave_Request.objects.create(name = userName, email = str(logger), from_date = from_date, to_date = to_date, reason = reason, leave_type = leave_type, total_days = LeaveDay,selectleave=selectleave)
                            leaveRequest.save()
                            print("===111===111==")
                            
                            aw.Custom_Festival_Leave = Remainigleave
                            aw.save()
                            print("===--- leave apply ---===")
                            return JsonResponse({'data':'===--- leave apply ---==='})

                        elif selectleave == 'full day':

                            leaveRequest = Leave_Request.objects.create(name = userName, email = str(logger), from_date = from_date, to_date = to_date, reason = reason, leave_type = leave_type, total_days = leaveDay,selectleave=selectleave)
                            leaveRequest.save()
                            # print("===111===111==")
                            aw.Custom_Festival_Leave = remainingLeave
                            aw.save()
                            # print("===--- leave apply ---===")
                            return JsonRespons
                        else:
                            print("====enter leave======")

                    else:
                        sd = []
                        for i in leaverequest:

                                if i.from_date <=start_date <= i.to_date:
                                    sd.append(i.from_date)
                                else:
                                    pass

                        if not sd :

                            # if  int(leave_days) <= int(ab):
                                print('=====fis===selectleave=========',selectleave)

                                if selectleave == 'first half':
                                    print('======FS=========',selectleave)
                                    if (halfleave_day) <= int(ab):
                                        leaveRequest = Leave_Request.objects.create(name = userName, email = str(logger), from_date = from_date, to_date = to_date, reason = reason, leave_type = leave_type, total_days = LeaveDay,selectleave=selectleave)
                                        leaveRequest.save()
                                        
                                        aw.Custom_Festival_Leave = Remainigleave
                                        aw.save()
                                        print("===> first half leave apply  <===")
                                        return JsonResponse({'data':'===> half leave apply <==='})
                                    
                                    else:
                                        print('==== you have no required leave =======')
                                
                                elif selectleave == 'second half':

                                    if (halfleave_day) <= int(ab):
                                        leaveRequest = Leave_Request.objects.create(name = userName, email = str(logger), from_date = from_date, to_date = to_date, reason = reason, leave_type = leave_type, total_days = LeaveDay,selectleave=selectleave)
                                        leaveRequest.save()
                                        
                                        aw.Custom_Festival_Leave = Remainigleave
                                        aw.save()
                                        print("===> second half leave apply  <===")
                                        return JsonResponse({'data':'===> half leave apply <==='})
                                    
                                    else:
                                        print('==== you have no required leave =======')
                                
                                elif selectleave == 'full day':
                                    print('========selectleavttttte=========',selectleave)
                                    if  int(leave_days) <= (ab):

                                        leaveRequest = Leave_Request.objects.create(name = userName, email = str(logger), from_date = from_date, to_date = to_date, reason = reason, leave_type = leave_type, total_days = leaveDay,selectleave=selectleave)
                                        leaveRequest.save()
                                        
                                        aw.Custom_Festival_Leave = remainingLeave
                                        aw.save()
                                        print("===> full leave apply <===")
                                        return JsonResponse({'data':'===> full leave apply <==='})
                                    
                                    else:
                                        print(f"<-----you have only {ab} days and you are applying {leaveDay} days---->")
                                        return JsonResponse({'data':'<----you have only{ab} days and you are applying {leaveDay}---->'})
                                        
                                else:
                                    print("---==select leave==---")
                            # else:
                            #     print(f"<-----you have only {ab} days and you are applying {leaveDay} days---->")
 
                        else:   
                            print("======>>>>>>=========")
                            return JsonResponse({'data':"leave already apply on this date"})
                except:
                    print("-=--=-=- except =--=-=-=")
                    return JsonResponse({'data':'-=--=-=- except =--=-=-='})
            else:
                print("<==== select leave type ====>")
                return JsonResponse({'data':'<==== select leave type ====>'})
        else:
            print(" <==start date must be less than end date===> ")
            return JsonResponse({'data':'<=== start date must be less than end date ===>'})

@csrf_exempt
def werty(request):

    if request.method == 'POST':
        
        logger = request.user
        status = request.POST.get('status')
        leave = Leave_Request.objects.all().filter(email=logger)

        if status == 'Accept':
        #    qwerty = Leave_Request.objects.filter(email=logger).update(status='Accept')
            for i in leave:
                pass
            i.status = 'Accept'
            i.save()
        
        elif status == 'Reject':

            for i in leave:
                pass
            i.status = 'Reject'
            i.save()
            leavedays = i.total_days 
            leavetype = i.leave_type
            name = i.name
            print("====leavetype===",leavetype)
            print("===total==",type(leavedays))
             

            cd = 'Custom_Festival_Leave'
            aw = LeaveType_with_LeaveBalance.objects.all().filter(username=name)
            x = leavedays.split()
            print(x[0],type(x[0]))

            for j in aw:

                j.Custom_Festival_Leave = j.Custom_Festival_Leave + float(x[0])  
                j.save()
            # leave.delete()
        else:
            print("=====not updated=====")

@csrf_exempt
def recuritment(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone_no = request.POST.get('phone_no')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        applying_for = request.POST.get('applying_for')
        experience = request.POST.get('experience')

        data = RecruitmentSystem.objects.filter(email = email)
        print('==data==',data)
        if data:
            print("==== user already exist ===")
            return JsonResponse({'data':'user email already registered'})
        
        else:
            recruit = RecruitmentSystem.objects.create(name = name, email= email, phone_no = phone_no, age = age, gender = gender, applying_for = applying_for, experience = experience)
            recruit.save()

            return JsonResponse({'data':'data register sucessfully'})

    else:
        print('--------request not from POST side -------')
        return JsonResponse({'data':'request not from POST side'})

@csrf_exempt
def candidate_interview(request):

    if request.method == "POST":

        job_applicant = request.POST.get('job_applicant')
        interviewRound = request.POST.get('interviewRound')
        designation = request.POST.get('designation')
        scheduledTime = request.POST.get('scheduledTime')
        from_time = request.POST.get('from_time')
        to_time = request.POST.get('to_time')
        status = request.POST.get('status')
        # job_applicant
        instant = RecruitmentSystem.objects.get(id = job_applicant)
        qw = instant.email
        print("====instant===",instant)

        current_date = datetime.now().date()
        try:

            data = interview.objects.all().filter(job_applicant=qw)
            print("=======data========",data)   
            if not data:
                interviewSchedule = interview.objects.create(job_applicant=instant,interviewRound=interviewRound,designation=designation,scheduledTime=scheduledTime,from_time=from_time,to_time=to_time,status=status)
                interviewSchedule.save()
                print("======= interviewSchedule ======",interviewSchedule)
                print("==== you sucessfully applied for round-1 interview ====",interviewSchedule)
            
            elif data:
                print("==========================")
                for i in data:
                    pass
                Round = i.interviewRound
                roundstatus = i.status
                scheduleDate = i.scheduledTime
                print("====i.schedule time=====",type(scheduleDate))
                
                a = time.mktime(time.strptime(str(scheduleDate), "%Y-%m-%d"))
                print("====a====",a)
                b = time.mktime(time.strptime(scheduledTime, "%Y-%m-%d"))
                print("====b=====",b)

                delta = b - a
                days = (delta/86400)+1
                print("=== type ====",leave_days,type(leave_days))
                reaplyTime = int(days)
                print("====leaveday====",reaplyTime)

                if Round == interviewRound:
                    if roundstatus == 'Cleared': 
                        print("=== you already cleared this round ==== ")

                    elif roundstatus == 'Rejected':
                        
                        if reaplyTime >= 90:
                            interviewSchedule = interview.objects.create(job_applicant=instant,interviewRound=interviewRound,designation=designation,scheduledTime=scheduledTime,from_time=from_time,to_time=to_time,status=status)
                            interviewSchedule.save()
                            print("=== you sucessfully aplly ===")
                        else:
                            print("===you can  not apply befor 90 days===")

                    else:
                        print("===== your interview is not cleared =====")

                elif Round != roundstatus:
                    interviewSchedule = interview.objects.create(job_applicant=instant,interviewRound=interviewRound,designation=designation,scheduledTime=scheduledTime,from_time=from_time,to_time=to_time,status=status)
                    interviewSchedule.save()
                    print("====elif=====")
                
                else:
                    print("=========]=========]==>")

                print("==round ==",Round)
                print("==== status ==",roundstatus)
                print("====i.id====",i.id)
                # if Round == 'round-1' and roundstatus == 'Cleared':
            
            else:
                print("==============================")
        
        except:               
            print("=== there is not data ===")

@csrf_exempt
def interviewStatus(request):

    if request.method == 'POST':

        ids = request.POST.get('ids')
        stat = request.POST.get('stat')
        print("====ids====",ids)
        # interview_object = interview.objects.get(id=ids)
        interview_object = interview.objects.all().filter(id=ids)

        print("=======interview_object =======",interview_object)
        for i in interview_object: 
            pass
            print("==== ")
        # print('=== status ====', status)
        if stat == 'Cleared':
            i.status = 'Cleared'
            i.save()    
        
        # elif status == 'rejected':
        #     interview_object.status = 'rejected'
        #     interview_object.save()
        # elif status == 'under review':
        #     interview_object.status = 'under review'
        #     interview_object.save()
        else:
            print("==== choose 3 of one ====")
    else:
        print("=======================")
        print("========================")