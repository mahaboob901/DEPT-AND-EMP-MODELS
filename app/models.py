from pickle import FALSE, TRUE
from django.db import models

# Create your models here.
class Department(models.Model):
    did=models.IntegerField(primary_key=TRUE)
    dname=models.CharField(max_length=100,null=FALSE)
    loc=models.CharField(max_length=100,null=FALSE)
class Employee(models.Model):
    eid=models.IntegerField(primary_key=TRUE)
    ename=models.CharField(max_length=100,null=False)
    job=models.CharField(max_length=100,null=False)
    sal=models.CharField(max_length=100,null=False)
    did=models.ForeignKey(Department,on_delete=models.CASCADE)
    

