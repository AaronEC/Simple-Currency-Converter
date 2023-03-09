from django import forms
  
# Form for error checking converter user input 
class InputForm(forms.Form):
    
    input_field = forms.FloatField()
