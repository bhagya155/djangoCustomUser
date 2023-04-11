from django.shortcuts import render,redirect
from django.contrib import messages
from . forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate, login,logout


# Create your views here.
def index(request):
    return render(request,"index.html")

def loginview(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_doctor:
                login(request, user)
                return redirect('doctor')
            elif user is not None and user.is_patient:
                login(request, user)
                return redirect('patient')
            
            else:
                messages.warning(request, 'invalid credentials')
                msg= 'invalid credentials'
        else:
            msg = 'error validating form'
            messages.warning(request, "Invalid Credentials")
    return render(request, 'loginview.html', {'form': form, 'msg': msg})

def register(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST,request.FILES)
        
        if form.is_valid():
            user = form.save()
            msg = 'user created'
            messages.success(request,'your account is created successfully')
            return redirect('loginview')
        else:
            messages.warning(request, form.errors)
            msg = 'form is not valid'
    else:
        form = SignUpForm()
    return render(request,'register.html', {'form': form, 'msg': msg})
def handlelogout(request):
    logout(request)
    messages.success(request, "Successfully Loged out")
    return redirect('index')

def doctor(request):
    return render(request,"doctor.html")
def patient(request):
    return render(request,"patient.html")
    