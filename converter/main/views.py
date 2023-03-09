import json
import os
from django.shortcuts import render

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
   
    return render(request, "index.html", {"currency":currency()})