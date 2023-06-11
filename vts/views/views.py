from django.shortcuts import render
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponse

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        # Отримати дані форми авторизації з POST-запиту
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Перевірка введених даних авторизації
        user = authenticate(request, email=email, password=password)
        if user is not None:
            # Успішна авторизація, виконати вхід користувача
            login(request, user)
            return HttpResponse('Успішний вхід!')
        else:
            # Помилка авторизації, повернути повідомлення про помилку
            return HttpResponse('Помилка авторизації!')

    else:
        # Відобразити сторінку авторизації (шаблон форми авторизації)
        return render(request, 'main/login.html')
    
def register_view(request):
    return render(request, 'main/register.html')

def index_view(request):
    return render(request, 'main/index.html')

def bracelets_view(request):
    return render(request, 'main/bracelets.html')

def services_view(request):
    return render(request, 'main/services.html')

def zones_view(request):
    return render(request, 'main/zones.html')

def settings_view(request):
    return render(request, 'main/settings.html')

def statistics_view(request):
    return render(request, 'main/statistics.html')

def visitors_view(request):
    return render(request, 'main/visitors.html')

def zones_view(request):
    return render(request, 'main/zones.html')