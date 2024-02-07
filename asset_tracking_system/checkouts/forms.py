
from django import forms
from .models import Checkout

class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Checkout
        fields = ['employee', 'device', 'expected_return_date', 'actual_return_date']
