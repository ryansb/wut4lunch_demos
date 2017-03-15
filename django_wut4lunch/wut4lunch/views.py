from django import forms
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import Lunch

# Create your views here.

class LunchForm(forms.Form):
    submitter = forms.CharField(label='Your name')
    food = forms.CharField(label='What did you eat?')


lunch_form = LunchForm(auto_id=False)

def index(request):
    lunches = Lunch.objects.all()
    return render(
        request,
        'wut4lunch/index.html',
        {
            'lunches': lunches,
            'form': lunch_form,
        }
    )

def newlunch(request):
    l = Lunch()
    l.submitter = request.POST['submitter']
    l.food = request.POST['food']
    l.save()
    return redirect('home')
