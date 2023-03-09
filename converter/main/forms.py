from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator
  
# Form for error checking converter user input 
class InputForm(forms.Form):
    
    input_field = forms.DecimalField(max_digits=100, decimal_places=2)
