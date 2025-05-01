from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
def home_view(request):
    return render(request, "home.html")

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Login successful, redirect to home
        else:
            messages.error(request, 'Invalid credentials. Please try again.')
            return render(request, 'accounts/login.html')  # Explicitly re-render login page
    return render(request, 'accounts/login.html')

def home_view(request):
    accounts = [
        {"name": "Artificial Intelligence", "image": "accounts/img/ai.jpg"},
        {"name": "Computer Science", "image": "accounts/img/cs.jpg"},
        {"name": "Electronics and Communication", "image": "accounts/img/ec.jpg"},
        {"name": "Chemical", "image": "accounts/img/chemical.jpg"},
        {"name": "Industrial Chemistry", "image": "accounts/img/industrial.jpg"},
        {"name": "Mechanical", "image": "accounts/img/mechanical.jpg"},
        {"name": "Civil", "image": "accounts/img/civil.jpg"},
        {"name": "Physics", "image": "accounts/img/physics.jpg"},
        {"name": "Mathematics", "image": "accounts/img/math.jpg"},
    ]
    return render(request, "accounts/home.html", {"accounts": accounts})

def mathematics_department(request):
    return render(request, 'accounts/mathematics-department.html')

def physics_department(request):
    return render(request, 'accounts/physics-department.html')

def civil_department(request):
    return render(request, 'accounts/civil-department.html')

def mechanical_department(request):
    return render(request, 'accounts/mechanical-department.html')

def industrial_chemistry_department(request):
    return render(request, 'accounts/industrial-chemistry-department.html')

def chemical_department(request):
    return render(request, 'accounts/chemical-department.html')

def ec_department(request):
    return render(request, 'accounts/ec-department.html')

def cs_department(request):
    return render(request, 'accounts/cs-department.html')

def ai_department(request):
    return render(request, 'accounts/ai-department.html')



