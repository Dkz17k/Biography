from django.shortcuts import render

def index(request):
    return render(request, 'biography/index.html')

def contato(request):
    return render(request, 'biography/contato.html')