from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from django.db.models import Sum

from .forms import AddDonationForm
from .models import Donation




def LandingPageView(request):
    bag_quantity = Donation.objects.all().aggregate(data=Sum('quantity'))
    institution_quantity = Donation.objects.all().aggregate(data=Sum('institution'))
    context = {'bag_quantity': bag_quantity,
               'institution_quantity': institution_quantity,
               }
    return render(request, 'Webpage/index.html', context)


def AddDonationView(request):
    if request.method == "POST":
        form = AddDonationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('Webpage/form-confirmation.html')
        ctx = {
        'form': form,
        }
        return render(request, 'Webpage/form.html', ctx)


def LoginView(request):
    return render(request, 'Webpage/login.html')


def RegisterView(request):
    return render(request, 'Webpage/register.html')
