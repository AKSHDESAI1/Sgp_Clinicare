from django.contrib.auth.forms import PasswordChangeForm, SetPasswordForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from .forms import UserRegisterForm, LoginForm, UserProfileForm, AdminProfileForm
from django.contrib import messages
from oClinicApp.models import Information, Contact
from django.contrib.auth.models import User

from django.contrib.auth.forms import UserChangeForm
def logout1(request):
    logout(request)
    messages.success(
        request, f'Successfully Log out')
    return redirect('/')


def home1(request):
    return render(request, 'basic/home.html')


def signin1(request):
    if request.method == 'POST':
        form1 = UserRegisterForm(request.POST)
        if form1.is_valid():
            form1.save()
            username = form1.cleaned_data.get('username')
            messages.success(
                request, f'Account Created for {username}!Now Please Login')
            # messages.success(
            #     request, f'Your account has been created! You are now able to log in')

            # return redirect('blog-home')
            return redirect('login1')
        messages.error(
            request, f'Something is wriong. Maybe your password do not match or email id is already exist. Please Try again. ')
        form = LoginForm()
        form1 = UserRegisterForm()

    else:
        form = LoginForm()
        form1 = UserRegisterForm()
    return render(request, 'account/login.html', {'form': form, 'form1': form1})


def login1(request):
    if request.method == 'POST':
        form = LoginForm(request=request, data=request.POST)
        context = {
            'form': form
        }
        if form.is_valid():
            messages.success(request, 'Successfully Created Account ...')
            print('a1', request.user)
            return redirect('info')
        messages.error(request, 'Wrong Credentials. Please Try again ...')
        # form = UserRegisterForm()
    form = LoginForm()
    form1 = UserRegisterForm()
    context = {
        'form': form,
        'form1': form1
    }
    return render(request, template_name='account/login.html', context=context)


def info(request):
    if request.method == 'POST':
        username = request.POST['username']
        gender1 = request.POST['gender1']
        date1 = request.POST['date1']
        blood1 = request.POST['blood1']
        dia1 = request.POST['dia1']
        medical = request.POST['medical']
        allergies = request.POST['allergies']

        var1 = Information(username=request.user.username, gender1=gender1, date1=date1,
                           blood1=blood1, dia1=dia1, medical=medical, alergies=allergies)
        var1.save()
        messages.success(request, 'Your Information page is successfully saved. ')
        return redirect('/')
    else:
        userabc = ""
        if request.user.is_authenticated:
            userabc = request.user.username
        return render(request, 'basic/information.html', {"userabc": userabc})


def profile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            username = Information.objects.get(username=request.user)

            username.gender1 = request.POST['gender1']
            username.date1 = request.POST['date1']
            username.blood1 = request.POST['blood1']
            username.dia1 = request.POST['dia1']
            username.medical = request.POST['medical']
            username.alergies = request.POST['allergies']
            username.save()
            messages.success(request, 'Your Profile page is Successfully updated.')
            return redirect('/')

        userabc = ""
        if request.user.is_authenticated:
            userabc = request.user.username
            print('a', userabc)
            a = Information.objects.get(username=userabc)
            # username = a.username

            if a.gender1 == 'male1':
                gender = True
            else:
                gender = False

            if a.blood1 == 'yes':
                blood = True
            else:
                blood = False

            if a.dia1 == 'yes':
                dia = True
            else:
                dia = False

            context = {
                'username': a.username,
                'gender': gender,
                'date': a.date1.strftime("%Y-%m-%d"),
                # 'date': a.date1,
                'blood': blood,
                'dia': dia,
                'medical': a.medical,
                'alergies': a.alergies

            }
            print(context)
            print(
                f'{a.username} {a.gender1} {a.date1.strftime("%y-%m-%d")} {a.blood1} {a.dia1} {a.medical} {a.alergies}')
            return render(request, 'basic/profile.html', context)
        return render(request, 'basic/profile.html')
    else:
        return HttpResponseRedirect('/404_Error/')

def connection(request):
    return render(request, 'basic/connection.html')

def migrane_chat(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/signin1/')
    else:
        if request.method == 'POST':
            return HttpResponse('meow99')
        return render(request, 'basic/migrane_chat.html')

def heartattack_chat(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/signin1/')
    return render(request, 'basic/heartattack_chat.html')

def covid_19(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/signin1/')
    return render(request, "basic/covid19.html")

def diabetes(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/signin1/')
    return render(request, "basic/diabetes.html")


def error(request):
    return render(request, 'basic/404.html')

def about(request):
    return render(request, 'basic/about.html')

def contact(request):
    if request.method == 'POST':
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        email = request.POST['email']
        subject = request.POST['subject']
        a = Contact(first_name=first_name, last_name=last_name, email = email, subject = subject)
        a.save()
        messages.success(request, 'Your Data has been Successfully Saved. ')
        return HttpResponseRedirect('/')

    else:
        return render(request, 'basic/contact.html')

def checkup(request):
    return render(request, 'basic/checkup.html')

def profile1(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm = UserProfileForm(request.POST, instance = request.user)
            if fm.is_valid():
                fm.save()
                messages.success(request, 'Your Personal Profile has been Updated Successfully.')
                return HttpResponseRedirect('/')
        else:
            if request.user.is_superuser:
                fm = AdminProfileForm(instance = request.user)
                users = User.objects.all()
            else:
                fm = UserProfileForm(instance = request.user)
                users = None
        return render(request, 'basic/profile1.html', {'form': fm, 'users': users})
    else:
        return HttpResponseRedirect('/404_Error/')

def thyroid(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/signin1/')
    return render(request, 'basic/thyroidchat.html')

def changepassword(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm = PasswordChangeForm(data = request.POST, user = request.user)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request, fm.user)
                messages.success(request, 'Your Password has been Successfully Updated.')
                return HttpResponseRedirect('/')
        else:
            fm = PasswordChangeForm(user = request.user)
        return render(request, 'basic/changepassword.html', {'form': fm})
    else:
        return HttpResponseRedirect('/404_Error/')


def forgotpassword(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm = SetPasswordForm(data = request.POST, user = request.user)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request, fm.user)
                messages.success(request, 'Your Password has been Successfully Updated.')
                return HttpResponseRedirect('/')
        else:
            fm = SetPasswordForm(user = request.user)
        return render(request, 'basic/forgotpassword.html', {'form': fm})
    else:
        return HttpResponseRedirect('/404_Error/')

def detail(request, my_id):
    if request.user.is_superuser:
        my_id = User.objects.get(id = my_id)
        if request.method == 'POST':
            fm = AdminProfileForm(data = request.POST, instance = my_id)
            if fm.is_valid():
                fm.save()
                messages.success(request, f"{my_id.username}'s Profile has been updated Successfully.")
                return HttpResponseRedirect('/profile1/')
        else:
            fm = AdminProfileForm(instance = my_id)
        return render(request, 'basic/detail.html', {'form': fm, 'users': my_id})
    else:
        return HttpResponseRedirect('/404_Error/')

def changepassword1(request, my_id1):
    if request.user.is_superuser:
        my_id = User.objects.get(username = my_id1)
        if request.method == 'POST':
            fm = SetPasswordForm(data = request.POST, user = my_id)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request, fm.user)
                messages.success(request, f"{my_id}'s Password has been updated Successfully")
                return HttpResponseRedirect('/profile1/')
        else:
            fm = SetPasswordForm(user = my_id)
        return render(request, 'basic/changepassword1.html', {'form': fm, 'users': my_id})
    else:
        return HttpResponseRedirect('/404_Error/')