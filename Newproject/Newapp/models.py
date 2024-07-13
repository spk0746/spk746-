from django.db import models

# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=100, null=True)
    Age=models.IntegerField(default=0)
    Address=models.CharField(max_length=100, null=True)
    Mobile=models.IntegerField(default=0)
    Email=models.CharField(max_length=50, null=True)
    
    def __str__ (self):
        return self.name+" "+str(self.Age) # type: ignore