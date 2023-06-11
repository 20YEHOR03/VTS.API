from django.urls import path, include
from .views.views import login_view, register_view, index_view, bracelets_view, services_view, zones_view, settings_view, statistics_view, visitors_view, zones_view

urlpatterns = [
    # Інші маршрути вашого проекту
    path('', login_view, name='login_view'),
    path('register', register_view, name='register_view'),
    path('index', index_view, name='index_view'),
    path('bracelets', bracelets_view, name='bracelets_view'),
    path('services', services_view, name='services_view'),
    path('zones', zones_view, name='zones_view'),
    path('settings', settings_view, name='settings_view'),
    path('statistics', statistics_view, name='statistics_view'),
    path('visitors', visitors_view, name='visitors_view'),
    path('zones', zones_view, name='visitors_view'),
]