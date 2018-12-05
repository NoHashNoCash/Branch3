from django.shortcuts import render
import csv, io
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from .models import Transaction
from django.urls import reverse
from django.contrib import messages
import re

class TransactionDetailView(DetailView):
    model = Transaction



class TransactionCreateView(CreateView):
    model = Transaction
    fields = ['vendor','amount','type']

    def form_valid(self, form):
        form.instance.user = self.request.user

        if form.cleaned_data['type'] != 'N' and form.cleaned_data['type'] != 'F' and form.cleaned_data['type'] != 'S':
            form.add_error(None,"Type Must be Either N for necessities, F for Fun, S for Savings")
            return self.form_invalid(form)

        return super(TransactionCreateView,self).form_valid(form)

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('save-progress')

class TransactionUpdateView(UpdateView):
    model = Transaction
    fields = ['vendor', 'amount', 'type']

    def form_valid(self,form):
        form.instance.user = self.request.user

        if form.cleaned_data['type'] != 'N' and form.cleaned_data['type'] != 'F' and form.cleaned_data['type'] != 'S':
            form.add_error(None, "Type Must be Either N for necessities, F for Fun, S for Savings")
            return self.form_invalid(form)

        return super(TransactionUpdateView,self).form_valid(form)

    def get_success_url(self):
        return reverse('save-transactions')

class TransactionDeleteView(DeleteView):
    model = Transaction

    def get_success_url(self):
        return reverse('save-transactions')

def transaction_upload(request):
    template = "transactions/transaction_upload.html"

    prompt = {
        'order': 'order of CSV is Vendor, Amount, Type'
    }

    if request.method == 'GET':
        return render(request, template, prompt)

    csv_file = request.FILES['file']


   # if not csv_file.name.endswith('.csv'):
  #      messages.error(request,'file is not a csv file')

    #  data_set = csv_file.read().decode("UTF-8")

      #print(data_set)

     #io_string = io.StringIO(data_set)
     # print(io_string)
     # for column in csv.reader(data_set, delimiter=',', quotechar='|'):
         # _, created = Transaction.objects.update_or_create(
        #      user = request.user,
       #      vendor=column[0],
      #       amount=column[1],
     #         type=column[2]
    #      )
   #   context = {}
  #return render(request, template, context)

