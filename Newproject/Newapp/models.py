from django.db import models

# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=100, null=True)
    age=models.IntegerField(default=0)
    address=models.CharField(max_length=100, null=True)
    mobile=models.IntegerField(default=0)
    email=models.CharField(max_length=50, null=True)
    
    def __str__ (self):
        return self.name+" "+str(self.age)+" "+self.address+" "+str(self.mobile)+" "+self.email+" "