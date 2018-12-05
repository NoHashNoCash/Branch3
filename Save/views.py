from django.shortcuts import render
from django.http import HttpResponse
from . import views
from transactions.models import Transaction
from budget.models import Budget
# Create your views here.

def home(request):
    return render(request,'Save/home.html',{})

def transactions(request):
    queryresults = Transaction.objects.filter(user=request.user)


    results = [
        {

            'queryresults': queryresults,
        }
    ]

    context = {
        'results': results

    }

    return render(request,'Save/transactions.html',context)

def progress(request):

    queryresults = Transaction.objects.filter(user=request.user)
    necessitiestotal = 0
    funtotal = 0
    savingstotal = 0

    for i in queryresults:
        if i.type == 'N':
            necessitiestotal = necessitiestotal + i.amount
        if i.type == 'S':
         savingstotal = savingstotal + i.amount
        if i.type == 'F':
            funtotal = funtotal + i.amount

    totalspent = necessitiestotal + savingstotal + funtotal

    necessitiespercent = int((necessitiestotal / totalspent) * 100)
    savingspercent = int(savingstotal / totalspent * 100)
    funpercent = int(funtotal / totalspent * 100)


    print(funtotal)

    results = [
        {
            'necessitiespercent': necessitiespercent,
            'savingspercent': savingspercent,
            'funpercent': funpercent,
            'necessitiestotal':  necessitiestotal,
            'funtotal':  funtotal,
            'savingstotal': savingstotal,
            'queryresults': queryresults,
            'budgetresults': Budget.objects.filter(user=request.user),
        }
    ]

    context = {
        'results': results

    }
    return render(request,'Save/progress.html',context)