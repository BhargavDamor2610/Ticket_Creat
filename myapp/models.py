from django.db import models

# Create your models here.
class DEPARTMENT(models.Model):
    Name=models.CharField(max_length=50)
    Description=models.TextField(null=True)
    def __str__ (self):
        return self.Name

class USER(models.Model):
    Department = models.ForeignKey(DEPARTMENT,on_delete=models.CASCADE,null=True)
    Name=models.CharField(max_length=50)
    Email=models.EmailField(unique=True)
    Mobile_Number=models.CharField(max_length=12,unique=True)
    Password=models.CharField(max_length=15)
    Role=models.CharField(max_length=20)
    def __str__ (self):
        return self.Name