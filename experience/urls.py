from . import views
from django.urls import path

urlpatterns = [
    # path('', views.test, name='experience'),
    path('mixins/', views.ExperienceMixinApiView.as_view()),
    path('mixins/<int:pk>/', views.ExperienceMixinApiView.as_view()),
]
