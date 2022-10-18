from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.db.models import Sum
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.views import View
from django.core.exceptions import ValidationError

from .models import Donation, Institution, CustomUser, Category
from .forms import  AddDonationForm, SignUpForm2



def myOrdersView(request):

    return render(request, 'Webpage/MyOrders.html')



def formConfirmation(request):
    if request.user.is_authenticated:
        return render(request, "Webpage/form-confirmation.html")


def infoUsers(request):
    if request.user.is_authenticated:
        context = {}
        return render(request, "Webpage/infoUser.html", context)


def LandingPageView(request):
    bag_quantity = Donation.objects.all().aggregate(data=Sum('quantity'))
    institution_quantity = Donation.objects.all().aggregate(data=Sum('institution'))
    institution_foundation = Institution.objects.filter(type=3)
    institution_organization = Institution.objects.filter(type=2)
    institution_local = Institution.objects.filter(type=1)
    context = {'bag_quantity': bag_quantity,
               'institution_quantity': institution_quantity,
               'institution_foundation': institution_foundation,
               'institution_organization': institution_organization,
               'institution_local': institution_local,
               }
    return render(request, 'Webpage/index.html', context)


def AddDonationView(request):
    if request.user.is_authenticated:
        categories = Category.objects.all()
        if request.method == "POST":
            form = AddDonationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('my-order')
        else:
            form = AddDonationForm()

        context = {
            'categories': categories,
            'form': form
        }
        return render(request, 'Webpage/form.html', context)
    else:
        messages.success(request, ("Musisz się zalogować!"))
        return redirect('login')

def LogoutView(request):
    logout(request)
    messages.success(request, ("Log out"))
    return redirect('landing-page')


def LoginView(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user_exists = CustomUser.objects.filter(email=email).exists()
        user = authenticate(request, email=email, password=password)
        if user_exists:
            if user is not None:
                login(request, user)
                return redirect('landing-page')
            else:
                return redirect('login')
        else:
            return redirect('register')
    else:
        return render(request, 'Webpage/login.html')


# def RegisterView(request):
#     if request.method == "POST":
#         form = SignUpForm2(request.POST or None)
#         if form.is_valid():
#             cd = form.cleaned_data
#             password = cd.get('password1'),
#             password2 = cd.get('password2'),
#             email = cd.get('email'),
#             # email = cd['email'],
#             # first_name = cd['first_name'],
#             # last_name = cd['last_name'],
#             # password = cd['password1'],
#             # password2 = cd['password2'],
#             if password != password2:
#                 if CustomUser.objects.filter(email=email).exists():
#                     messages.info(request, "Taki email już istnieje.")
#                     return redirect('register')
#                 else:
#                     form.save()
#                     messages.success(request, "Utworzono konto :)")
#                     return redirect('login')
#             else:
#                 messages.error(request, ("Osoba o takim adresie email już istnieje, lub hasła są niepoprawne"))
#                 return redirect('register')
#         else:
#             form = SignUpForm2()
#     return render(request, 'Webpage/register.html', {'form': form})
#
#


# def RegisterView(request):
#     if request.method == "POST":
#         form = SignUpForm2(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('login')
#     form = SignUpForm2()
#     return render(request, 'Webpage/register.html', {'form': form})
#

def RegisterView(request):
    if request.method == "POST":
        form = SignUpForm2(request.POST)
        if form.is_valid():
            # cd = form.cleaned_data
            #
            # cu = CustomUser(
            # email = cd['email'],
            # first_name = cd['first_name'],
            # last_name = cd['last_name'],
            # password1 = cd['password1'],
            # password2 = cd['password2'],
            # )
            #
            # if CustomUser.objects.filter(email=cu.email).exists():
            #     raise ValidationError("Taki email już istnieje")
            #
            # # if cu.password != cu.:
            # #     raise ValidationError("Hasła nie są identyczne")

            form.save()
            return redirect('login')
    else:
        form = SignUpForm2()
    return render(request, 'Webpage/register.html', {'form': form})