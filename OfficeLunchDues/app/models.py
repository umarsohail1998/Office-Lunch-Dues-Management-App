from django.db import models

# Create your models here.

class Employees(models.Model):
    
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    gender = models.CharField(max_length=1)
    phone = models.CharField(max_length=15)
    age = models.IntegerField()
    address = models.CharField(max_length=255)
    salary = models.IntegerField()
    Date = models.DateField()
    
    def __str__(self):
        return self.full_name
    
    
class Record(models.Model):

    balance = models.IntegerField()
    date = models.DateTimeField()
    employee = models.ForeignKey(Employees, on_delete=models.CASCADE)

    # def __str__(self):
    #     return self.balance
    
    
class Monthly_Record(models.Model):
    dues = models.IntegerField()
    month = models.CharField(max_length=255)
    employee = models.ForeignKey(Employees, on_delete=models.CASCADE)
    
    # def __str__(self):
    #     return self.month