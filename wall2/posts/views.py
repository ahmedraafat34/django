from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from posts.forms import Entryform
from rest_framework import viewsets
from django.contrib.auth.forms import UserCreationForm
from .serializers import *
from .import serializers

class Entry (viewsets.ModelViewSet):
    queryset= Entry.objects.all()
    serializer_class = serializers.EntrySerializer

def index(request):

    posts = Entry.queryset.order_by('-date_posted')
    context = {'posts': posts}
    return render(request, 'posts/index.html', context)


def add(request):
    form = Entryform()

    if request.method == 'POST':
        form = Entryform(request.POST)

    if form.is_valid():
        form.save()
        return redirect('home')
    else:
        form = Entryform()

        context = {'form': form}
    return render(request, 'posts/add.html', context)

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    form = UserCreationForm()
    return render(request,'registration/signup.html' , {
        'form' : form
    })