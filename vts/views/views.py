from django.shortcuts import render
from django.shortcuts import render

# Create your views here.
def login_view(request):
    return render(request, 'main/login.html')
    
def register_view(request):
    return render(request, 'main/register.html')

def index_view(request):
    return render(request, 'main/index.html')

def bracelets_view(request):
    return render(request, 'main/bracelets.html')

def bracelet_add_view(request):
    return render(request, 'main/bracelet-add.html')

def bracelet_edit_view(request, bracelet_id):
    return render(request, 'main/bracelet-edit.html', {'bracelet_id': bracelet_id})

def zones_view(request):
    return render(request, 'main/zones.html')

def zone_add_view(request):
    return render(request, 'main/zone-add.html')

def zone_edit_view(request, zone_id):
    return render(request, 'main/zone-edit.html', {'zone_id': zone_id})

def services_view(request):
    return render(request, 'main/services.html')

def service_add_view(request):
    return render(request, 'main/service-add.html')

def service_edit_view(request, service_id):
    return render(request, 'main/service-edit.html', {'service_id': service_id})

def settings_view(request):
    return render(request, 'main/settings.html')

def statistics_view(request):
    return render(request, 'main/statistics.html')

def visitors_view(request):
    return render(request, 'main/visitors.html')

def visitor_add_view(request):
    return render(request, 'main/visitor-add.html')

def visitor_edit_view(request, customuser_id):
    return render(request, 'main/visitor-edit.html', {'customuser_id': customuser_id})