from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from . models import Details
from . models import Contact
from django.contrib import messages

# Create your views here.
def home(request):

    return render(request,'home.html')

def contact(request):
    FirstName=request.POST.get('FirstName', False)
    LastName=request.POST.get('LastName', False)
    Email=request.POST.get('Email', False)
    Subject=request.POST.get('Subject', False)
    Message=request.POST.get('Message', False)

    c=Contact(FirstName= FirstName,LastName=LastName,Email=Email,Subject=Subject,Message=Message)
    c.save()
    return render(request,'contact.html')
    

def categories(request):
    return render(request,'categories.html')
    
@login_required(login_url="/login/")  
def checkout(request):
    if request.method == 'POST':
        Name=request.POST.get('Name', False)
        Address=request.POST.get('Address', False)
        Country=request.POST.get('Country', False)
        City=request.POST.get('City', False)
        Item=request.POST.get('Item', False)
        Phone=request.POST.get('Phone', False)
        p=Details(Name=Name,Address=Address,Country=Country,City=City,Item=Item,Phone=Phone)
        p.save()
        return redirect('thankyou')
    else:     
        return render(request,'checkout.html')

def bag1(request):
    return render(request,'bag1.html')

def bag2(request):
    return render(request,'bag2.html')

def bag3(request):
    return render(request,'bag3.html')

def bag4(request):
    return render(request,'bag4.html')
    
def shoe4(request):
    return render(request,'shoe4.html')

def shoe3(request):
    return render(request,'shoe3.html')

def shoe2(request):
    return render(request,'shoe2.html')

def shoe1(request):
    return render(request,'shoe1.html')

def dress1(request):
    return render(request,'dress1.html')

def dress2(request):
    return render(request,'dress2.html')

def dress3(request):
    return render(request,'dress3.html')

def dress4(request):
    return render(request,'dress4.html')

def acc1(request):
    return render(request,'acc1.html')

def acc2(request):
    return render(request,'acc2.html')

def acc3(request):
    return render(request,'acc3.html')

def acc4(request):
    return render(request,'acc4.html')
    
def thankyou(request):
    return render(request,'thankyou.html')

def about(request):
    return render(request,'about.html')




def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user =form.save()
            #logtheuser
            login(request,user)
            messages.success(request,f'Account created for {user}!')
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request,'signup.html',{'form':form})


def login_view(request):
    if request.method == 'POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
        
            #logtheuser
            user = form.get_user()
            login(request,user)
            messages.success(request,f'Logged in Succesfully!')
            return redirect('home')
    else:
        form =AuthenticationForm()
    return render(request,'login.html',{'form':form})    

def logout_view(request):
    if request.method == 'POST':   
        logout(request) 
        messages.success(request,f'Logged out Succesfully!')
        return redirect('home')    


@login_required(login_url="/login/")
def shopcreate(request):
    return render(request,'shopcreate.html')  




      