from django.contrib.auth import authenticate, login
from django.core.checks import messages
from django.shortcuts import render, redirect

# Create your views here.
from app1.forms import Form
from app1.models import Login


def home(request):
    return render(request, 'home.html')


def user_register(request):
    login_form = Form()
    if request.method == 'POST':
        login_form = Form(request.POST, request.FILES)
        if login_form.is_valid():
            user = login_form.save(commit=False)
            user.is_user = True
            user.save()
            return redirect('home')
    return render(request, 'user_register.html', {'login_form': login_form})


def user_panel(request):
    data = Login.objects.filter(is_user=True)
    return render(request, 'user_panel.html', {'data': data})


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_user:
                return redirect('user_panel')
        else:
            messages.info(request, 'INVALID CREDENTIALS')
    return render(request, 'login.html')


