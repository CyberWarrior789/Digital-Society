import email
from django.shortcuts import render,redirect
from .models import *
from MemberApp.models import *
from Watchman.models import *
from django.core.mail import send_mail
from random import randint,choice

# Create your views here.
count = 0
def login(request):
    global count
    if "email" in request.session:
        uid = User.objects.get(email = request.session['email'])
        if uid.role == "Chairman":
            cid = Chairman.objects.get(user_id = uid)
            gender = cid.gender
            mcount = Member.objects.all().count()
            ncount = Notice.objects.all().count()
            ecount = Event.objects.all().count()
            c_count = Complain.objects.all().count()
            context = {
                        'uid':uid,
                        'cid':cid,
                        'gender':gender,
                        'mcount':mcount,
                        'ncount':ncount,
                        'ecount':ecount,
                        'c_count':c_count,
                    }
            return render(request,"Chairman/index.html",{'context':context})
        elif uid.role == "Member":
            mid = Member.objects.get(user_id = uid)
            gender = mid.gender
            mcount = Member.objects.all().count()
            ncount = Notice.objects.all().count()
            ecount = Event.objects.all().count()
            c_count = Complain.objects.all().count()
            context = {
                        'uid':uid,
                        'mid':mid,
                        'gender':gender,
                        'mcount':mcount,
                        'ncount':ncount,
                        'ecount':ecount,
                        'c_count':c_count,
                    }
            return render(request,"MemberApp/Mindex.html",{'context':context})
        else:
            wid = Watchman.objects.get(user_id = uid)
            mcount = Member.objects.all().count()
            ncount = Notice.objects.all().count()
            ecount = Event.objects.all().count()
            c_count = Complain.objects.all().count()
            context = {
                        'uid':uid,
                        'wid':wid,
                        'mcount':mcount,
                        'ncount':ncount,
                        'ecount':ecount,
                        'c_count':c_count,
                    }
            return render(request,"Watchman/Windex.html",{'context':context})
    if request.POST:
        try:
            p_email = request.POST['email']
            p_password = request.POST['password']

            uid = User.objects.get(email = p_email)

            if uid:
                if uid.password == p_password:
                    if uid.role == "Chairman":
                        count = 0
                        cid = Chairman.objects.get(user_id = uid)
                        gender = cid.gender
                        mcount = Member.objects.all().count()
                        ncount = Notice.objects.all().count()
                        ecount = Event.objects.all().count()
                        c_count = Complain.objects.all().count()
                        context = {
                                    'uid':uid,
                                    'cid':cid,
                                    'gender':gender,
                                    'mcount':mcount,
                                    'ncount':ncount,
                                    'ecount':ecount,
                                    'c_count':c_count,
                                }
                        request.session['email'] = uid.email
                        if cid.gender == "Male":
                            cid.profile_pic = "media/defaultm.png"
                            cid.save()
                        elif cid.gender == "Female":
                            cid.profile_pic = "media/defaultf.png"
                            cid.save()
                        else:
                            cid.profile_pic = "media/default.png"
                            cid.save()
                        return render(request,"Chairman/index.html",{'context':context})
                    elif uid.role == "Member":
                        mid = Member.objects.get(user_id = uid)
                        if uid.first_login == False:
                            email = uid.email
                            otp = randint(1111,9999)
                            uid.otp = otp
                            uid.save()
                            msg1 = "Dear"+mid.firstname+","
                            msg = "\nYour otp is :"+str(otp)+", and is valid for 2 minutes."
                            send_mail("Super City - OTP",msg1+msg,"kahanchokshi07@gmail.com",[email])
                            return render(request,"MemberApp/Motp.html",{'email':email})
                        else:
                            count = 0
                            gender = mid.gender
                            mcount = Member.objects.all().count()
                            ncount = Notice.objects.all().count()
                            ecount = Event.objects.all().count()
                            c_count = Complain.objects.all().count()
                            context = {
                                        'uid':uid,
                                        'mid':mid,
                                        'gender':gender,
                                        'mcount':mcount,
                                        'ncount':ncount,
                                        'ecount':ecount,
                                        'c_count':c_count,
                                    }
                            request.session['email'] = uid.email
                            if mid.gender == "Male":
                                mid.profile_pic = "media/defaultm.png"
                                mid.save()
                            elif mid.gender == "Female":
                                mid.profile_pic = "media/defaultf.png"
                                mid.save()
                            else:
                                mid.profile_pic = "media/default.png"
                                mid.save()
                            return render(request,"MemberApp/Mindex.html",{'context':context})
                    else:
                        wid = Watchman.objects.get(user_id = uid)
                        uid.first_login = True
                        uid.is_verified = True
                        uid.save()
                        count = 0
                        mcount = Member.objects.all().count()
                        ncount = Notice.objects.all().count()
                        ecount = Event.objects.all().count()
                        c_count = Complain.objects.all().count()
                        context = {
                                    'uid':uid,
                                    'wid':wid,
                                    'mcount':mcount,
                                    'ncount':ncount,
                                    'ecount':ecount,
                                    'c_count':c_count,
                                }
                        request.session['email'] = uid.email
                        return render(request,"Watchman/Windex.html",{'context':context})
                else:
                    count+=1
                    e_msg = "invalid password"
                    if count>2:
                        e_msg = "You Entered Multiple Time Wrong Password. Crate Your New Password"
                        return render(request,"Chairman/forgotpassword.html",{'e_msg':e_msg})
                    return render(request,"Chairman/login.html",{'e_msg':e_msg})
            else:
                return render(request,"Chairman/login.html")
        except:
            e_msg="invalid email or password"
            return render(request,"Chairman/login.html",{'e_msg':e_msg})
    else:
        return render(request,"Chairman/login.html")

def logout(request):
    if "email" in request.session:
        del request.session['email']
        return redirect('login')
    else:
        return redirect('login')

def cprofile(request):
    if "email" in request.session:
        uid = User.objects.get(email = request.session['email'])

        if request.POST:
            cpassword = request.POST['cpassword']
            npassword = request.POST['npassword']
            if uid.password == cpassword:
                uid.password = npassword
                uid.save()
                return redirect('Cprofile')
        else:
            if uid.role == "Chairman":
                cid = Chairman.objects.get(user_id = uid)
                gender = cid.gender
                mcount = Member.objects.all().count()
                ncount = Notice.objects.all().count()
                ecount = Event.objects.all().count()
                c_count = Complain.objects.all().count()
                context = {
                            'uid':uid,
                            'cid':cid,
                            'gender':gender,
                            'mcount':mcount,
                            'ncount':ncount,
                            'ecount':ecount,
                            'c_count':c_count,
                        }
                return render(request,"Chairman/Cprofile.html",{'context':context})
            else:
                pass
    else:
        return redirect('login')

def index(request):
    return redirect('login')

def forgot_password(request):
    if request.POST:
        email = request.POST['email']
        otp = randint(1111,9999)
        uid = User.objects.get(email = email)
        try:
            if uid:
                uid.otp = otp
                uid.save()
                cid = Chairman.objects.get(user_id = uid)
                msg1 = "Dear"+cid.firstname+","
                msg = "\nYour otp is :"+str(otp)+", and is valid for 2 minutes."
                send_mail("Super City - OTP",msg1+msg,"kahanchokshi07@gmail.com",[email])
                return render(request,"Chairman/otp.html",{'email':email})
        except:
            e_msg = "email does not exist"
            return render(request,"Chairman/forgot_password.html",{'e_msg':e_msg})
    else:
        return render(request,"Chairman/forgot_password.html")

def otp(request):
    if request.POST:
        email = request.POST['email']
        otp = request.POST['otp']
        uid = User.objects.get(email = email)
        if uid:
            if str(uid.otp) == otp and uid.email == email:
                return render(request,"Chairman/reset-password.html",{'email':email})
            else:
                e_msg = "invalid otp"
                return render(request,"Chairman/otp.html",{'e_msg':e_msg})
    else:
        e_msg = "Time Out"
        return render(request,"Chairman/forgot_password.html",{'e_msg':e_msg})

def reset_password(request):
    if request.POST:
        email = request.POST['email']
        npassword = request.POST['npassword']
        cpassword = request.POST['cpassword']
        uid = User.objects.get(email = email)
        if uid:
            if npassword == cpassword:
                uid.password = cpassword
                uid.first_login = True
                uid.is_verified = True
                uid.save()
                return redirect('login')
            else:
                e_msg = "!! newpassword & confirmpassword does not match !!"
                return render(request,"Chairman/reset-password.html",{'e_msg':e_msg})
    else:
        return redirect('forgot_password')

def add_member(request):
    if "email" in request.session:
        uid = User.objects.get(email = request.session['email'])
        cid = Chairman.objects.get(user_id = uid)
        l1 = ["aasa34","45asd546","456dsv","8098sd","dsf35f"]
        if request.POST:
            email = request.POST['email']
            password = email[:4]+choice(l1)
            role = "Member"
            house_no = request.POST['house_no']
            uid = User.objects.create(email = email,password = password,role = role)
            hid = House.objects.get(house_no = house_no)
            hid.status = "Owned"
            hid.save()
            mid = Member.objects.create(
                            user_id = uid,
                            house_id = hid,
                            firstname = request.POST['fname'],
                            lastname = request.POST['lname'],
                            mobileno = request.POST['mobileno'],
                            job_specification = request.POST['job specification'],
                            job_address = request.POST['job_address'],
                            birthdate = request.POST['birthdate'],
                            no_of_members = request.POST['no_of_members'],
                            marrital_status = request.POST['m_status'],
                            locality = request.POST['locality'],
                            nationality = request.POST['nationality'],
                            gender = request.POST['gender'],
                            no_of_vehicles = request.POST['no_of_vehicles'],
                            vehicle_type = request.POST['vehicle_type'],
                            id_proof = request.FILES['id_proof'],
                        )
            if mid:
                msg = "Your Password is :"+password
                send_mail("Welcome to Super City",msg,"kahanchokshi07@gmail.com",[email])
                m_all = Member.objects.all()
                gender = cid.gender
                context = {
                            'uid':uid,
                            'cid':cid,
                            'gender':gender,
                        }
                return render(request,"Chairman/view-member.html",{'context':context})
        else:
            gender = cid.gender
            house_all = House.objects.filter(status = "Pending")
            m_all = Member.objects.all()
            mcount = Member.objects.all().count()
            ncount = Notice.objects.all().count()
            ecount = Event.objects.all().count()
            c_count = Complain.objects.all().count()
            context = {
                        'uid':uid,
                        'cid':cid,
                        'gender':gender,
                        'house_all':house_all,
                        'm_all':m_all,
                        'mcount':mcount,
                        'ncount':ncount,
                        'ecount':ecount,
                        'c_count':c_count,
                    }
            return render(request,"Chairman/add-member.html",{'context':context})
    else:
        return redirect('login')

def view_member(request):
    if "email" in request.session:
        uid = User.objects.get(email = request.session['email'])
        cid = Chairman.objects.get(user_id = uid)
        gender = cid.gender
        house_all = House.objects.all()
        m_all = Member.objects.all()
        mcount = Member.objects.all().count()
        ncount = Notice.objects.all().count()
        ecount = Event.objects.all().count()
        c_count = Complain.objects.all().count()
        context = {
                    'uid':uid,
                    'cid':cid,
                    'gender':gender,
                    'house_all':house_all,
                    'm_all':m_all,
                    'mcount':mcount,
                    'ncount':ncount,
                    'ecount':ecount,
                    'c_count':c_count,
                }
        return render(request,"Chairman/view-member.html",{'context':context})

def add_notice(request):
    if "email" in request.session:
        if request.POST:
            uid = User.objects.get(email = request.session['email'])
            if "pic" in request.FILES and "video" not in request.FILES:
                nid = Notice.objects.create(
                    user_id = uid,
                    title = request.POST['title'],
                    desc = request.POST['desc'],
                    pic = request.FILES['pic'],
                )
            elif "video" in request.FILES and "pic" not in request.FILES:
                nid = Notice.objects.create(
                    user_id = uid,
                    title = request.POST['title'],
                    desc = request.POST['desc'],
                    video = request.FILES['video'],
                )
            elif "pic" in request.FILES and "video" in request.FILES:
                nid = Notice.objects.create(
                    user_id = uid,
                    title = request.POST['title'],
                    desc = request.POST['desc'],
                    pic = request.FILES['pic'],
                    video = request.FILES['video'],
                )
            else:
                nid = Notice.objects.create(
                    user_id = uid,
                    title = request.POST['title'],
                    desc = request.POST['desc'],
                )
            return redirect('view-notice')
        else:
            uid = User.objects.get(email = request.session['email'])
            cid = Chairman.objects.get(user_id = uid)
            gender = cid.gender
            mcount = Member.objects.all().count()
            ncount = Notice.objects.all().count()
            ecount = Event.objects.all().count()
            c_count = Complain.objects.all().count()
            context = {
                        'uid':uid,
                        'cid':cid,
                        'gender':gender,
                        'mcount':mcount,
                        'ncount':ncount,
                        'ecount':ecount,
                        'c_count':c_count,
                    }
            return render(request,"Chairman/add-notice.html",{'context':context})
    else:
        return redirect('login')

def add_events(request):
    if "email" in request.session:
        if request.POST:
            uid = User.objects.get(email = request.session['email'])
            if "pic" in request.FILES and "video" not in request.FILES:
                eid = Event.objects.create(
                    user_id = uid,
                    title = request.POST['title'],
                    desc = request.POST['desc'],
                    pic = request.FILES['pic'],
                )
            elif "video" in request.FILES and "pic" not in request.FILES:
                eid = Event.objects.create(
                    user_id = uid,
                    title = request.POST['title'],
                    desc = request.POST['desc'],
                    video = request.FILES['video'],
                )
            elif "pic" in request.FILES and "video" in request.FILES:
                eid = Event.objects.create(
                    user_id = uid,
                    title = request.POST['title'],
                    desc = request.POST['desc'],
                    pic = request.FILES['pic'],
                    video = request.FILES['video'],
                )
            else:
                eid = Event.objects.create(
                    user_id = uid,
                    title = request.POST['title'],
                    desc = request.POST['desc'],
                )
            return redirect('view-events')
        else:
            uid = User.objects.get(email = request.session['email'])
            cid = Chairman.objects.get(user_id = uid)
            gender = cid.gender
            mcount = Member.objects.all().count()
            ncount = Notice.objects.all().count()
            ecount = Event.objects.all().count()
            c_count = Complain.objects.all().count()
            context = {
                        'uid':uid,
                        'cid':cid,
                        'gender':gender,
                        'mcount':mcount,
                        'ncount':ncount,
                        'ecount':ecount,
                        'c_count':c_count,
                    }
            return render(request,"Chairman/add-events.html",{'context':context})
    else:
        return redirect('login')


def view_notice(request):
    if "email" in request.session:
        uid = User.objects.get(email = request.session['email'])
        cid = Chairman.objects.get(user_id = uid)
        n_all = Notice.objects.all().order_by('created_at').reverse()
        gender = cid.gender
        mcount = Member.objects.all().count()
        ncount = Notice.objects.all().count()
        ecount = Event.objects.all().count()
        c_count = Complain.objects.all().count()
        context = {
                    'uid':uid,
                    'cid':cid,
                    'gender':gender,
                    'n_all':n_all,
                    'mcount':mcount,
                    'ncount':ncount,
                    'ecount':ecount,
                    'c_count':c_count,
                }
        return render(request,"chairman/view-notice.html",{'context':context})
    else:
        return redirect('login')

def view_events(request):
    if "email" in request.session:
        uid = User.objects.get(email = request.session['email'])
        cid = Chairman.objects.get(user_id = uid)
        e_all = Event.objects.all()
        gender = cid.gender
        mcount = Member.objects.all().count()
        ncount = Notice.objects.all().count()
        ecount = Event.objects.all().count()
        c_count = Complain.objects.all().count()
        context = {
                    'uid':uid,
                    'cid':cid,
                    'gender':gender,
                    'e_all':e_all,
                    'mcount':mcount,
                    'ncount':ncount,
                    'ecount':ecount,
                    'c_count':c_count,
                }
        return render(request,"chairman/view-events.html",{'context':context})
    else:
        return redirect('login')

def view_complain(request):
    if "email" in request.session:
        uid = User.objects.get(email = request.session['email'])
        cid = Chairman.objects.get(user_id = uid)
        com_all = Complain.objects.all()
        gender = cid.gender
        mcount = Member.objects.all().count()
        ncount = Notice.objects.all().count()
        ecount = Event.objects.all().count()
        c_count = Complain.objects.all().count()
        context = {
                    'uid':uid,
                    'cid':cid,
                    'gender':gender,
                    'com_all':com_all,
                    'mcount':mcount,
                    'ncount':ncount,
                    'ecount':ecount,
                    'c_count':c_count,
                }
        return render(request,"chairman/view-complain.html",{'context':context})
    else:
        return redirect('login')

def all_watchman(request):
    if "email" in request.session:
        uid = User.objects.get(email = request.session['email'])
        cid = Chairman.objects.get(user_id = uid)
        wall = Watchman.objects.all()
        context = {
                    'uid':uid,
                    'cid':cid,
                    'wall':wall,
        }
        return render(request,"Chairman/all-watchman.html",{'context':context})

def approved(request,pk):
    if "email" in request.session:
        uid = User.objects.get(email = request.session['email'])
        cid = Chairman.objects.get(user_id = uid)
        wid = Watchman.objects.get(user_id = pk)
        wemail = wid.user_id.email
        wid.status = "Approved"
        wid.save()
        msg = "Congratulations you have been Approved by Chairman Mr."+cid.firstname
        send_mail("Welcome to Super City",msg,"kahanchokshi07@gmail.com",[wemail])
        return redirect('all-watchman')
    else:
        return redirect('login')


def rejected(request,pk):
    if "email" in request.session:
        uid = User.objects.get(email = request.session['email'])
        cid = Chairman.objects.get(user_id = uid)
        wid = Watchman.objects.get(id = pk)
        wemail = wid.user_id.email
        wid.status="Rejected"
        wid.save()
        msg = "Sorry you have been Rejected by Chairman Mr."+cid.firstname
        send_mail("Welcome to Super City",msg,"kahanchokshi07@gmail.com",[wemail])
        return redirect('all-watchman')
    else:
        return redirect('login')

def del_notice(request,pk):
    if "email" in request.session:
        uid = User.objects.get(email = request.session['email'])
        cid = Chairman.objects.get(user_id = uid)
        nid = Notice.objects.get(id = pk)
        nid.delete()
        return redirect('view-notice')
    else:
        return redirect('login')