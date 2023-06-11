from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title='Your API Title',
        default_version='v1',
        description='Your API Description',
        terms_of_service='https://www.example.com/terms/',
        contact=openapi.Contact(email='contact@example.com'),
        license=openapi.License(name='BSD License'),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('organization/', include('vts.routing.organization_urls')),
    path('zone/', include('vts.routing.zone_urls')),
    path('service/', include('vts.routing.service_urls')),
    path('interaction/', include('vts.routing.interaction_urls')),
    path('bracelet/', include('vts.routing.bracelet_urls')),
    path('customuser/', include('vts.routing.customuser_urls')),
    path('api-auth/', include('rest_framework.urls')),
]