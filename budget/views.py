from django.shortcuts import render, redirect
from budget.models import Budget
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView
from django.forms import ModelForm,ValidationError
from django.urls import reverse,reverse_lazy

class budgetForm(ModelForm):
    class Meta:
        model = Budget
        fields = ['monthly_income', 'necessity_pct', 'savings_pct', 'fun_pct']

    def clean(self):
        cleaned_data = super(budgetForm, self).clean()

        monthly = cleaned_data.get('monthly_income')
        necessity = cleaned_data.get('necessity_pct')
        savings = cleaned_data.get('necessity_pct')
        fun = cleaned_data.get('fun_pct')


        print(necessity)
        print(savings)
        print(fun)


        total = necessity + savings + fun

        print(total)

        if necessity is not None and savings is not None and fun is not None:

            if total != 100:
                self.add_error(None, ValidationError("Necessity, Savings, and Fun percentages must add to 100"))

        return cleaned_data



class BudgetCreateView(LoginRequiredMixin, CreateView):
    model = Budget
    fields = ['monthly_income','necessity_pct','savings_pct','fun_pct']

    def form_valid(self,form):
        form.instance.user = self.request.user
        if form.cleaned_data['necessity_pct'] + form.cleaned_data['savings_pct'] + form.cleaned_data['fun_pct'] != 100:
            form.add_error(None, "Necessity, Savings, and Fun percentages must add to 100")
            return self.form_invalid(form)
        return super(BudgetCreateView, self).form_valid(form)

    def test_func(self):
        budget = self.get_object( )

    def get_success_url(self):
        return reverse('transaction-create')

class BudgetUpdateView(UpdateView):
    model = Budget
    fields = ['monthly_income', 'necessity_pct', 'savings_pct', 'fun_pct']

    def form_valid(self,form):
        form.instance.user = self.request.user
        if form.cleaned_data['necessity_pct'] +  form.cleaned_data['savings_pct'] + form.cleaned_data['fun_pct'] != 100:
            form.add_error(None,"Necessity, Savings, and Fun percentages must add to 100")
            return self.form_invalid(form)
        return super(BudgetUpdateView,self).form_valid(form)
    def get_success_url(self):
        return reverse('save-progress')


