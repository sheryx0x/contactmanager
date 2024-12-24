
from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from .models import *


def home(request):
    contacts = Contact.objects.all()
    return render(request,'contactmanagerapp/home.html', {'contacts':contacts})


def create_contact(request):
    if request.method == 'POST':
        form = contactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = contactForm()
        context = {'form':form}
        return render(request ,'contactmanagerapp/create_contact.html' ,context)
    
    
    
def update_contact(request, pk):
    contacts = Contact.objects.get(id=pk)
    if request.method == 'POST':
        form = contactForm(request.POST , instance=contacts)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = contactForm(instance=contacts)
        context = {'form':form,'contacts':contacts}
        return render(request ,'contactmanagerapp/update_contact.html',context)
    
    
    
def delete_contact(request,pk):
    contacts = Contact.objects.get(id=pk)
    contacts.delete()
    return redirect('home')


