from django.urls import path
from . import views
urlpatterns = [
    path('mixins/', views.AcademicMixinApiView.as_view()),
]
