from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from app.EmailBackEnd import EmailBackEnd
from django.contrib.auth import authenticate, login, logout
from app.models import Categories


def  REGISTER(request):
    category = Categories.get_all_category(Categories)
    context = {
        'category': category,
    }
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        #check email
        if User.objects.filter(email=email).exists():
            messages.warning(request, 'Email ini sudah pernah digunakan, masukkan email lain')
            return redirect('register')
        #check username
        elif User.objects.filter(username=username).exists():
            messages.warning(request, 'Username ini sudah pernah digunakan, masukkan username lain')
            return redirect('register')

        user = User(
            username=username,
            email=email,

        )
        user.set_password(password)
        user.save()
        return redirect('login')

    return render(request, 'registration/register.html', context)

def DO_LOGIN(request):

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = EmailBackEnd.authenticate(request, username=email, password=password)


        if user != None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Email dan Password salah')
            return redirect('login')

def PROFILE(request):
    category = Categories.get_all_category(Categories)
    context = {
        'category': category,
    }
    if request.user.is_authenticated:
        return render(request, 'registration/profile.html', context)
    else:
        return redirect('login')

def PROFILE_UPDATE(request):
    if request.method == "POST":
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_id = request.user.id

        user = User.objects.get(id=user_id)
        user.first_name = first_name
        user.last_name = last_name
        user.username = username
        user.email = email

        if password != None and password != "":
            user.set_password(password)
        user.save()
        messages.success(request, 'Profile telah berhasil di-Update. ')
        return redirect('profile')


def LOGOUT(request):
    logout(request)
    return redirect('home')