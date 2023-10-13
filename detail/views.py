from django.shortcuts import render
from django.shortcuts import render,redirect,HttpResponse
# Create your views here.
def home(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def edu(request):
    return render(request,'qualification.html')

def certification(request):
    return render(request,'certification.html')
#import contact data
from . models import Contact_user
def contactform(request):
    if request.method=="POST":
      name_h=request.POST.get('name')
      email_h=request.POST.get('email')
      contact_h=request.POST.get('contact')
      message_h=request.POST.get('message')

      print('hemlll')
      print(name_h)
      print(email_h)
      print(contact_h)
      print(message_h)
      cont=Contact_user(
         name=name_h,
         email=email_h,
         Contact=contact_h,
         message=message_h
           )
      cont.save()
    #return redirect('home')
    return render(request,'contact.html')

def project(request):
    return render(request,'project.html')