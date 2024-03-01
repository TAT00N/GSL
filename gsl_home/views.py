# En el archivo gsl_home/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def home_view(request):
    return render(request, 'gsl/home.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            next_url = request.POST.get('next', 'lista_cargas')  # Obtén la URL de redirección
            return redirect(next_url)

    return render(request, 'gsl/home.html')