from django.contrib import admin
from .models import ClientReq, ClientType, Payment,Cabin,Customer

# Register your models here.
admin.site.register(ClientReq)
admin.site.register(ClientType)
admin.site.register(Payment)
admin.site.register(Cabin)
admin.site.register(Customer)