from django.shortcuts import render,redirect
from .models import *
from Chairman.models import *
from MemberApp.models import *
from django.core.mail import send_mail

# Create your views here.
def sign_up(request):
    if request.POST:
            email = request.POST['email']
            paswd = request.POST['pass']
            cpass = request.POST['cpass']
            role = "Watchman"
            if paswd == cpass:
                uid = User.objects.create(email = email,password = cpass,role = role)
                wid = Watchman.objects.create(
                                user_id = uid,
                                firstname = request.POST['fname'],
                                lastname = request.POST['lname'],
                                id_proof = request.FILES['id-proof'],
                            )
                if wid:
                    msg = "You have been Successfully registered, You will be able to login when you will be Approved by Chairman"
                    send_mail("Welcome to Super City",msg,"kahanchokshi07@gmail.com",[email])
                    context = {
                                'uid':uid,
                                'wid':wid,
                            }
                    return render(request,"Watchman/sign-up.html",{'context':context})
            else:
                e_msg = "invalid password"
                return render(request,"Watchman/sign-up.html",{'e_msg':e_msg})
    else:
        return render(request,"Watchman/sign-up.html")

def wprofile(request):
    if "email" in request.session:
        uid = User.objects.get(email = request.session['email'])

        if request.POST:
            cpassword = request.POST['cpassword']
            npassword = request.POST['npassword']
            if uid.password == cpassword:
                uid.password = npassword
                uid.save()
                return redirect('Wprofile')
        else:
            if uid.role == "Watchman":
                wid = Watchman.objects.get(user_id = uid)
                context = {
                            'uid':uid,
                            'wid':wid,
                        }
                return render(request,"Watchman/Wprofile.html",{'context':context})
            else:
                pass
    else:
        return redirect('login')

def wview_member(request):
    if "email" in request.session:
        uid = User.objects.get(email = request.session['email'])
        wid = Watchman.objects.get(user_id = uid)
        m_all = Member.objects.all()
        context = {
                    'uid':uid,
                    'wid':wid,
                    'm_all':m_all,
                }
        return render(request,"Watchman/Wview-member.html",{'context':context})

def wview_notice(request):
    if "email" in request.session:
        uid = User.objects.get(email = request.session['email'])
        wid = Watchman.objects.get(user_id = uid)
        n_all = Notice.objects.all().order_by('created_at').reverse()
        context = {
                    'uid':uid,
                    'wid':wid,
                    'n_all':n_all,
                }
        return render(request,"Watchman/Wview-notice.html",{'context':context})
    else:
        return redirect('login')

def wview_events(request):
    if "email" in request.session:
        uid = User.objects.get(email = request.session['email'])
        wid = Watchman.objects.get(user_id = uid)
        e_all = Event.objects.all()
        context = {
                    'uid':uid,
                    'wid':wid,
                    'e_all':e_all,
                }
        return render(request,"Watchman/Wview-events.html",{'context':context})
    else:
        return redirect('login')

def add_visitor(request):
    if "email" in request.session:
        if request.POST:
            house_no = request.POST['house_no']
            hid = House.objects.get(house_no = house_no)
            vid = Visitor.objects.create(
                            hid = hid,
                            firstname = request.POST['fname'],
                            lastname = request.POST['lname'],
                            email = request.POST['email'],
                            mobileno = request.POST['mobileno'],
                            reason = request.POST['reason'],
                        )
            return redirect('view-visitor')
        else:
            uid = User.objects.get(email = request.session['email'])
            wid = Watchman.objects.get(user_id = uid)
            house_all = House.objects.all()
            context = {
                        'uid':uid,
                        'wid':wid,
                        'house_all':house_all,
                    }
            return render(request,"Watchman/add-visitor.html",{'context':context})
    else:
        return redirect('login')

def edit_visitor(request):
    if "email" in request.session:
        uid = User.objects.get(email = request.session['email'])
        wid = Watchman.objects.get(user_id = uid)
        context = {
                    'uid':uid,
                    'wid':wid,
                }
        return render(request,"Watchman/edit-visitor.html",{'context':context})
    else:
        return redirect('login')

def view_visitor(request):
    if "email" in request.session:
        uid = User.objects.get(email = request.session['email'])
        wid = Watchman.objects.get(user_id = uid)
        v_all = Visitor.objects.all()
        context = {
                    'uid':uid,
                    'wid':wid,
                    'v_all':v_all,
                }
        return render(request,"Watchman/view-visitor.html",{'context':context})