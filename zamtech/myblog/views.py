from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse
from django.template.loader import render_to_string, engines
from .postingform import postingForm
from django import forms


def index(request):
    return render(request, 'index.html') #just render template

def posting(request):
    if request.method == 'POST':
        form = postingForm(request.POST)
        if form.is_valid():
            #posting a post
            form.save()
            return redirect('/')
    else:
        form = postingForm()
    return render(request, 'postingform.html', {'form':postingForm})