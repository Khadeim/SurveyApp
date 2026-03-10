import re
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import CutomUserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
from .models import *


def loginUser(request):

    if request.user.is_authenticated:
        return redirect('home')

    msg = None

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                msg = 'User/Something is wrong'

        except:
            msg = 'User not recognized.'

    context = {
        'msg': msg
    }

    return render(request, 'user/login.html', context)


def register(request):

    msg = None
    form = CutomUserCreationForm()

    if request.method == 'POST':
        try:
            form = CutomUserCreationForm(request.POST)

            if form.is_valid():
                user = form.save(commit=False)
                user.save()

                sni = request.POST.get('SNI')
                address = request.POST.get("address")
                dob = request.POST.get('DOB')

                if UserInfo.objects.filter(sni_number=sni).exists():
                    sni_error = "Sni already exists"
                    context = {'form': form, 'sni_error': sni_error}
                    return render(request, 'user/register.html', context)

                userinfo = UserInfo.objects.create(
                    user=user,
                    sni_number=sni,
                    address=address,
                    date_of_birth=dob
                )

                userinfo.save()
                return redirect('login')

            else:
                msg = 'Error.'

        except:
            context = {'form': form, 'msg': msg, "snimsg": "Invalid SNI"}
            return render(request, 'user/register.html', context)

    context = {'form': form, 'msg': msg}
    return render(request, 'user/register.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')

def verify_sni(request):
    sni = request.GET.get("SNI")

    if sni and len(sni) >= 8:
        return JsonResponse({"status": "success"})
    else:
        return JsonResponse({"status": "error"})