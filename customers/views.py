from django.shortcuts import render, redirect
from .models import Customer #ClientReq, ClientType, Payment
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def index(request):
    customers = Customer.objects.all()

    # check to see if logging in
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']

        #Authenticate
        user =  authenticate(request, username = username,
        password = password)

        if user is not None:
            login(request,user)
            messages.success(request,"You Have Been Logged In !")
            return redirect('index')
        else:
            messages.success(request, "There was an error logging in, Please try again.")
            return redirect('index')
    else:
        return render(request, 'index.html',{
            'customers': customers})

def login_user(request):
    pass

def logout_user(request):
    logout(request)
    messages.success(request,"You Have Been Logged Out...")
    return redirect('index')