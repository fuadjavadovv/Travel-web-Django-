from urllib import request
from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm, UserChangeForm
from django.contrib.auth import login, logout

from user.forms import Registerform

# Create your views here.
def login_page(request):
    form = AuthenticationForm()
    if request.method == 'POST':
         form = AuthenticationForm(request, data=request.POST)
         if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
        
     
    return render(request, 'login.html', context={
        'form': form
    })


def register_page(request):
   form = Registerform()
   if request.method == "POST":
    form = Registerform(request.POST)
    if form.is_valid():
        form.save()
    return redirect('loginn')

   return render(request,'register.html',{'form':form})

def logout_page(request):
    logout(request)
    return redirect('index')

# def registerr(request):
#     form = Registerform()
#     if request.method == 'POST':
#         form = Registerform(request.POST)
#         if form.is_valid():
#             form.save()
#         return redirect('loginn')
#     return render(request,'reg')
        
