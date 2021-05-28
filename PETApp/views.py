from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from PETApp.form import CreateUserForm, PetRegisterForm
from .models import PetModel


# Create your views here.
def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('login')
    return render(request, 'UIComponent/reg.html', {'form': form})


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username OR password is incorrect')
    return render(request, "UIComponent/login.html", {})


def logoutUser(request):
    logout(request)
    return redirect('login')


def nav(request):
    return render(request, 'UIComponent/nav.html', {})


@login_required(login_url='login')
def homePage(request):
    return render(request, "UIComponent/home.html", {'datas': PetModel.objects.all()})


@login_required(login_url='login')
def petRegPage(request):
    form = PetRegisterForm()
    if request.method == 'POST':
        form = PetRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Pet Register Successfully')
            return redirect('petReg')
        else:
            messages.info(request, 'Pet Register not Successfully')
    return render(request, 'UIComponent/pet_register.html', {'form': form})


@login_required(login_url='login')
def display_page(request):
    return render(request, 'UIComponent/display.html', {'datas': PetModel.objects.all()})


@login_required(login_url='login')
def buy_pet(request, pk):
    return render(request, 'UIComponent/buy_pet.html', {'buy': PetModel.objects.all().get(pk=pk)})


@login_required(login_url='login')
def moreInfo(request, pk):
    return render(request, 'UIComponent/more.html', {'info': PetModel.objects.all().get(pk=pk)})


@login_required(login_url='login')
def successPage(request):
    return render(request, 'UIComponent/success.html', {})


@login_required(login_url='login')
def payment(request):
    return render(request, 'UIComponent/payment.html', {})


@login_required(login_url='login')
def about(request):
    return render(request, "UIComponent/about.html", {})


def about1(request):
    return render(request, "UIComponent/about1.html", {})


def getPet(request, pet):
    if request.method == 'POST':
        p = PetModel().objects.all().filter(type__in=pet.lower())
        if p is not None:
            return render(request, 'UIComponent/demo_filter.html', {'datas': p})
        else:
            messages.info(request, "Not Exist")
    return render(request, 'UIComponent/demo_filter.html', {'datas': []})
