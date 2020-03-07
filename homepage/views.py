from django.shortcuts import render

def index(request):
    """
    Return the index.html
    """
    
    return render(request, 'index.html')
