from django.shortcuts import render
from .models import Customer

# Create your views here.
def index(request):
    return render(request, 'Website/index.html',{
        'customer': Customer.objects.all()
    })