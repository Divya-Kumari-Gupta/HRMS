from django.db import models
from datetime import date
# Create your models here.
class Employee(models.Model):
    employeeId=models.AutoField
    username=models.CharField(max_length=14,primary_key=True)
    name=models.CharField(max_length=30,default="")
    email=models.EmailField()
    phoneNumber=models.BigIntegerField(default=+91 )
    age=models.IntegerField(default=0)
    department=models.CharField(max_length=30,default="")
    role=models.CharField(max_length=30,default="")
    salary=models.FloatField(default=0.0)
    leaves=models.IntegerField(default=0)
    joinDate=models.DateField(default=date.today())
    status=models.CharField(max_length=10,default="Inactive")

    def __str__(self):
        return self.username
