from multiprocessing import context
from django.shortcuts import render,redirect
from Chairman.models import *
from MemberApp.models import *
from random import randint
from django.core.mail import send_mail

# Create your views here.
def Mview_member(request):
    if "email" in request.session:
        uid = User.objects.get(email = request.session['email'])
        if uid.role == "Member":
            mid = Member.objects.get(user_id = uid)
            m_all = Member.objects.exclude(user_id = uid)
            gender = mid.gender
            context = {
                'uid':uid,
                'mid':mid,
                'm_all':m_all,
                'gender':gender,
            }
            return render(request,"MemberApp/Mview-member.html",{'context':context})

def Mprofile(request):
    if "email" in request.session:
        uid = User.objects.get(email = request.session['email'])

        if request.POST:
            cpassword = request.POST['cpassword']
            npassword = request.POST['npassword']
            if uid.password == cpassword:
                uid.password = npassword
                uid.save()
                return redirect('Mprofile')
        else:
            if uid.role == "Member":
                mid = Member.objects.get(user_id = uid)
                gender = mid.gender
                context = {
                            'uid':uid,
                            'mid':mid,
                            'gender':gender,
                        }
                return render(request,"MemberApp/Mprofile.html",{'context':context})
            else:
                pass
    else:
        return redirect('login')

def Madd_member(request):
    if "email" in request.session:
        uid = User.objects.get(email = request.session['email'])
        mid = Member.objects.get(user_id = uid)
        if request.POST:
            mid = Member.objects.get(user_id = uid)
            email = request.POST['email']
            password = email[:4]+"@"+mid.house_id.house_no
            role = "Member"
            locality = mid.locality
            uid = User.objects.create(email = email,password = password,role = role)
            famid = Member.objects.create(
                            user_id = uid,
                            member_id = mid,
                            firstname = request.POST['fname'],
                            lastname = request.POST['lname'],
                            mobileno = request.POST['mobileno'],
                            job_specification = request.POST['job specification'],
                            job_address = request.POST['job_address'],
                            birthdate = request.POST['birthdate'],
                            locality = locality,
                            nationality = request.POST['nationality'],
                            gender = request.POST['gender'],
                        )
        # if famid:
        #         msg = "Your Password is :"+password
        #         memail = request.session['email']
        #         send_mail("Welcome to Super City",msg,"kahanchokshi07@gmail.com",[memail])
        #         send_mail("Welcome to Super City",msg,"kahanchokshi07@gmail.com",[email])
        #         m_all = Member.objects.all()
        #         uid.first_login = True
        #         uid.is_verified = True
        #         uid.save()
        #         context = {
        #                 'uid':uid,
        #                 'mid':mid,
        #                 'm_all':m_all,
        #             }
        #         return render(request,"MemberApp/Madd-member.html",{'context':context})
        else:
            gender = mid.gender
            context = {
                'uid':uid,
                'mid':mid,
                'gender':gender,
            }
            return render(request,"MemberApp/Madd-member.html",{'context':context})
    else:
        return redirect('login')

def Madd_complain(request):
    if "email" in request.session:
        if request.POST:
            if "pic" in request.FILES and "video" not in request.FILES:
                cid = Complain.objects.create(
                    title = request.POST['title'],
                    desc = request.POST['desc'],
                    pic = request.FILES['pic'],
                )
            elif "video" in request.FILES and "pic" not in request.FILES:
                cid = Complain.objects.create(
                    title = request.POST['title'],
                    desc = request.POST['desc'],
                    video = request.FILES['video'],
                )
            elif "pic" in request.FILES and "video" in request.FILES:
                cid = Complain.objects.create(
                    title = request.POST['title'],
                    desc = request.POST['desc'],
                    pic = request.FILES['pic'],
                    video = request.FILES['video'],
                )
            else:
                cid = Complain.objects.create(
                    title = request.POST['title'],
                    desc = request.POST['desc'],
                )
            return redirect('Madd-complain')
        else:
            uid = User.objects.get(email = request.session['email'])
            mid = Member.objects.get(user_id = uid)
            gender = mid.gender
            context = {
                'uid':uid,
                'mid':mid,
                'gender':gender,
            }
            return render(request,"MemberApp/Madd-complain.html",{'context':context})
    else:
        return redirect('login')

def mview_notice(request):
    if "email" in request.session:
        uid = User.objects.get(email = request.session['email'])
        mid = Member.objects.get(user_id = uid)
        n_all = Notice.objects.all().order_by('created_at').reverse()
        context = {
                    'uid':uid,
                    'mid':mid,
                    'n_all':n_all,
                }
        return render(request,"MemberApp/Mview-notice.html",{'context':context})
    else:
        return redirect('login')

def mview_events(request):
    if "email" in request.session:
        uid = User.objects.get(email = request.session['email'])
        mid = Member.objects.get(user_id = uid)
        e_all = Event.objects.all()
        context = {
                    'uid':uid,
                    'mid':mid,
                    'e_all':e_all,
                }
        return render(request,"MemberApp/Mview-events.html",{'context':context})
    else:
        return redirect('login')