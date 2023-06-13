from django.urls import path
from .views import views
urlpatterns = [
    path('', views.login_view, name='login_view'),
    path('register/', views.register_view, name='register_view'),
    path('index/', views.index_view, name='index_view'),
    path('bracelets/', views.bracelets_view, name='bracelets_view'),
    path('bracelet/add', views.bracelet_add_view, name='bracelet_add_view'),
    path('bracelet/edit/<int:bracelet_id>', views.bracelet_edit_view, name='bracelet_edit_view'),
    path('zones/', views.zones_view, name='zones_view'),
    path('zone/add', views.zone_add_view, name='zone_add_view'),
    path('zone/edit/<int:zone_id>', views.zone_edit_view, name='zone_edit_view'),
    path('services/', views.services_view, name='services_view'),
    path('service/add', views.service_add_view, name='service_add_view'),
    path('service/edit/<int:service_id>', views.service_edit_view, name='service_edit_view'),
    path('settings/', views.settings_view, name='settings_view'),
    path('statistics/', views.statistics_view, name='statistics_view'),
    path('visitors/', views.visitors_view, name='visitors_view'),
    path('visitor/add', views.visitor_add_view, name='visitor_add_view'),
    path('visitor/edit/<int:customuser_id>', views.visitor_edit_view, name='visitor_edit_view'),
]