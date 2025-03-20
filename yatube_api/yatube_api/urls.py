from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

# Основные маршруты проекта
urlpatterns = [
    path('admin/', admin.site.urls),  # Админка Django
    path('api/', include('api.urls')),  # API endpoints
    path(
        'redoc/',
        TemplateView.as_view(template_name='redoc.html'),
        name='redoc'  # Документация Redoc
    ),
]
