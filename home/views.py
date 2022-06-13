from django.shortcuts import render,HttpResponse
from .models import Contact
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def report(request):
    return render(request,'report.html')
def blog(request):
    return render(request,'blogs.html')
def pictures(request):
    return render(request,'pictures.html')
def contact(request):
    if request.method=="POST":
        name= request.POST.get('name')
        print(name)
        email= request.POST.get('email')
        print(email)
        phone= request.POST.get('phone')
        print(phone)
        desc= request.POST.get('desc')
        print(desc)
        contact=Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
        messages.success(request, 'Your message has been sent!')
    return render(request, 'contact.html')
  

