"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # add all the urls from api/urls.py after the localhost -> localhost:8000/api/
    path('api/', include('api.urls')),
    # add all the urls from diary/urls.py after the localhost -> localhost:8000/api/diary/
    path('api/diary/', include('diary.urls')),
    # add all the urls from metadata/urls.py after the localhost -> localhost:8000/api/metadata/
    path('api/metadata/', include('metadata.urls')),
    # add all the urls from experience/urls.py after the localhost -> localhost:8000/api/experience/
    path('api/experience/', include('experience.urls')),
    # add all the urls from education/urls.py after the localhost -> localhost:8000/api/education/
    path('api/education/', include('education.urls')),
    # add all the urls from academic/urls.py after the localhost -> localhost:8000/api/academic/
    path('api/academic/', include('academic.urls')),
    # add all the urls from cerule/urls.py after the localhost -> localhost:8000/api/cerule/
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
