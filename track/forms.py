from django import forms
from .models import Expense


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ('name', 'amount', 'category')
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'amount': forms.NumberInput(attrs={'class':'form-control'}),
            'category': forms.TextInput(attrs={'class':'form-control'})
        }