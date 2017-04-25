from django.shortcuts import render,redirect
from .forms import SignupForm
from django.contrib.auth.models import User
from django.http import HttpResponse
# Create your views here.

def index(request):

    return render(request, 'landing/index.html')



def login():
    pass


def signup(request):
    form = SignupForm(request.POST or None)
    if request.method == 'POST':
        
        print(form.is_valid())
        if form.is_valid():
            form.cleaned_data.pop('confirm_password', None)
            user = User.objects.create_user(**form.cleaned_data)
            user.save()
            return redirect("landing:index")
    
    return render(request,'landing/sign.html',{'sign':form})
            
    


def logout():
    pass

