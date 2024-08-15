from django.urls import path
from . import views




urlpatterns = [
    path('first/',views.home),
    path('Add/',views.UserAdd),
    path('allusers/',views.AllUsers),
    path('Register',views.Register,name="Register"),
]