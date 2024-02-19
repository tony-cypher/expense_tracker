from django.shortcuts import render, redirect
from django.db.models import Sum
from .forms import ExpenseForm
from .models import Expense
import datetime

# Create your views here.

def index(request):
    if request.method == 'POST':
        expense = ExpenseForm(request.POST)
        if expense.is_valid():
            expense.save()
    expenses = Expense.objects.all()
    total_expenses = expenses.aggregate(Sum('amount'))

    # Calulation of 365 days
    last_year = datetime.date.today() - datetime.timedelta(days=365)
    year_data = Expense.objects.filter(date__gt=last_year)
    yearly_sum = year_data.aggregate(Sum('amount'))

    # last 30 days
    last_month = datetime.date.today() - datetime.timedelta(days=30)
    month_data = Expense.objects.filter(date__gt=last_month)
    monthly_sum = month_data.aggregate(Sum('amount'))

    # last 7 days
    last_week = datetime.date.today() - datetime.timedelta(days=7)
    week_data = Expense.objects.filter(date__gt=last_week)
    weekly_sum = week_data.aggregate(Sum('amount'))

    # categorical
    categorical_sum = Expense.objects.filter().values('category').order_by('category').annotate(sum=Sum('amount'))
    expense_form = ExpenseForm()
    context = {
        'expense_form':expense_form,
        'expenses':expenses, 
        'total_expenses':total_expenses,
        'yearly_sum':yearly_sum,
        'monthly_sum':monthly_sum,
        'weekly_sum': weekly_sum,
        'categorical_sum': categorical_sum
    }
    return render(request, 'track/index.html', context)

def edit(request, id):
    expense = Expense.objects.get(id=id)
    expense_form = ExpenseForm(instance=expense)
    if request.method == 'POST':
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'track/edit.html', {'expense_form':expense_form})

def delete(request, id):
    expense = Expense.objects.get(id=id)
    expense.delete()
    return redirect('index')