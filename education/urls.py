from django.urls import path
from . import views
urlpatterns = [
    path('mixins/', views.EducationMixinApiView.as_view()),
]
