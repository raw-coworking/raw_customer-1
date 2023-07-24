from django.shortcuts import render, redirect
from .models import Customer #ClientReq, ClientType, Payment
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import AddRecordForm

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

def customer_record(request, pk):
     if request.user.is_authenticated:
         customer_record = Customer.objects.get(id = pk)
         return render(request, 'record.html',{'customer_record': customer_record})
     
     else:
         messages.success(request, "You Must Be Logged In To View That Page...")
         return redirect('index')


def delete_record(request, pk):
	if request.user.is_authenticated:
		delete_it = Customer.objects.get(id = pk)
		delete_it.delete()
		messages.success(request, "Record Deleted Successfully !")
		return redirect('index')
	else:
		messages.success(request, "You Must Be Logged In To Do That !")
		return redirect('index')


def add_record(request):
     form = AddRecordForm(request.POST or None)
     if request.user.is_authenticated:
          if form.is_valid():
               add_record = form.save()
               messages.success(request,"Record added...")
               return redirect('index')
          return render(request,'add_record.html',{'form': form})
     else:
          messages.success(request,"You must be logged In...")
     return render(request,'index')

def update_record(request, pk):
	if request.user.is_authenticated:
		current_record = Customer.objects.get(id=pk)
		form = AddRecordForm(request.POST or None, instance=current_record)
		if form.is_valid():
			form.save()
			messages.success(request, "Record Has Been Updated!")
			return redirect('index')
		return render(request, 'update_record.html', {'form':form})
	else:
		messages.success(request, "You Must Be Logged In...")
		return redirect('index')