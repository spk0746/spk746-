from django.shortcuts import render

from .models import User
#from Newproject.Newapp.forms import User_form
from .forms import User_form


# Create your views here.

def home(request):
  data={'name':'praveen',
        'age':'25',
        'mobile':'9962378732',
        'email':'praveenselvaraj2510@gmail.com',
        'address':'Chennai'
        }
  return render(request,'index.html',data)


def UserAdd(request):
  form=User_form()
  
  if request.method == 'POST':
    form=User_form(request.POST)
    if form.is_valid():
      form.save()
  return render(request,'User_add.html',{'form':form})    
  
  
def AllUsers(request):
    Userinfo=User.objects.all()
    return render(request,'Alluser.html',{'all':Userinfo})