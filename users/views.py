from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from . import views
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from budget.models import Budget

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST);
        if form.is_valid():
            form.save()
            messages.success(request, f'Account Created! You are now able to login')
            return redirect('budget-create')
    else:
        form = UserRegisterForm();
    return render(request,'users/register.html',{'form':form})

@login_required
def profile(request):

    context = {
        'results': Budget.objects.filter(user=request.user)
    }
    return render(request,'users/profile.html',context)



