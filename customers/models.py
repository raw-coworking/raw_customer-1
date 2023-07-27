from django.db import models

# Create your models here.
class ClientReq(models.Model):
    type = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.type

class ClientType(models.Model):
    type = models.CharField(max_length=100, null=False)
    
    def __str__(self):
        return self.type

class Payment(models.Model):
    type = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.type

class Cabin(models.Model):
    Cabin_Studio = models.CharField(max_length=100, null =False)

    def __str__(self):
        return self.Cabin_Studio

class Customer(models.Model):
    # created_at = models.DateTimeField(auto_now_add=True, default=0)
    client_Type = models.ForeignKey(ClientType, on_delete=models.CASCADE)
    client_Req = models.ForeignKey(ClientReq,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    Place_Allotted = models.ForeignKey(Cabin, on_delete=models.CASCADE)
    no_of_seats = models.IntegerField(default=0)
    start_date = models.DateField()
    end_date = models.DateField()
    monthly_charges = models.IntegerField(default=0)
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE)
    security_amount = models.IntegerField(default=0)
    Lock_in_duration = models.CharField(max_length=100)
    payment_date = models.DateField()
    customer_Aadhaar = models.CharField(max_length=50)

    def __str__(self):
        return "%s, %s, %s, %s" %(self.first_name, self.last_name, self.email, self.phone)