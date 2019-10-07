from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .forms import UserLoginForm,UserSignUpForm
from cart.models import Order
from .models import Profile
# Create your views here.
def login_page(req):
    next = req.GET.get('next')
    form = UserLoginForm(req.POST or None)
    if form.is_valid():
        unm = form.cleaned_data.get('unm')
        pwrd = form.cleaned_data.get('pwrd')
        user = authenticate(username=unm,password=pwrd)
        if user:
            login(req,user)
            if next:
                return redirect(next)
        return redirect('/')
    return render(req,'accounts/login.html',{'form':form})

def logout_page(req):
    logout(req)
    return redirect('/')

def signup_page(req):
    next = req.GET.get('next')
    form = UserSignUpForm(req.POST or None)
    if form.is_valid():
        pwrd = form.cleaned_data.get('pwrd2')
        user = form.save(commit=False)
        user.set_password(pwrd)
        user.save()
        new_obj = authenticate(username=user.username,password=pwrd)
        if new_obj:
            login(req,new_obj)
            if next:
                return redirect(next)
        return redirect('/')
    return render(req,'accounts/signup.html',{'form':form})

def my_profile(req):
    my_user_profile = Profile.objects.filter(user=req.user).first()
    my_order        = Order.objects.filter(is_ordered=True,owner=my_user_profile)
    context = {
        'my_order':my_order,
    }
    return render(req,'accounts/profile.html',context)
