import json
import os
import requests

from django.shortcuts import render

from .forms import InputForm

def currency():
    """This imports the current currency list of data from a JSON

    Returns:
        dict: dict containing currency data.
    """
    
    json_dir = os.path.dirname(__file__)
    location = os.path.join(json_dir, 'currencies.json')

    with open(location, "r") as f:
        currency = json.loads(f.read())
        
    return currency

def index(request):
    """Main page view which has the coverter in it."""
    
    if request.method == "POST":

        # User input data is requested from HTML.
        input = request.POST.get('input')
        output = request.POST.get('output')
        form = InputForm(request.POST)
        amount = float(form['input_field'].value())
        
        # API call for the current exchange rate data.
        data = requests.get(f"https://open.er-api.com/v6/latest/{input}").json()
        
        # get amount to multiply input by.
        multiple = data['rates'][output]
        converted = format(float(multiple * amount),',.2f') # 2 decimal places
        
        context = {
            'converted': converted,
            'output': output,
            'input': input,
            'amount': amount,
            'currency': currency(),
            'form': InputForm(initial={'input_field': amount})
        }
        
        return render(request, "index.html", context)
        
    form = InputForm(initial={'input_field': 50})
        
    
    context = {
        'currency': currency(),
        'input': 'USD',     # These are the defaults
        'output': 'EUR',     # Currently the worlds most traded currencies
        'form': InputForm()
    }
   
    return render(request, "index.html", context)