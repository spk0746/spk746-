from django.shortcuts import render

#from Newproject.Newapp.forms import User_form
from .forms import User_form


# Create your views here.

def home(request):
  data={'name':'praveen',
        'role':'Developer',
        'mobile':'9962378732',
        'Email':'praveenselvaraj2510@gmail.com',
        'Address':'Chennai'
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
    User=User.objects.all()
    return render(request,'Alluser.html',{'all':User})