from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', views.api_home),
    path('create/', views.api_create),
    path('token/', obtain_auth_token)
]
