"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import include, path

from orders import views as orders_views

from triangle import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # Home task 6. Django: Hypotenuse calculator
    path('triangle/', include('triangle.urls')),
    # Home task 7. ModelForm for Person
    path('person/', views.create_person, name='person'),
    path('person/<int:pk>/', views.update_person, name='update-person'),
    # HT 12. Celery
    path('reminder/', orders_views.reminder, name='reminder'),
]

# HT 10. django-debug-toolbar, django silk
if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        path('__debug__', include(debug_toolbar.urls)),  # Add Debug Tollbar's URLconf
        path('silk/', include('silk.urls', namespace='silk')),  # Add Silk's URLconf
    ]
