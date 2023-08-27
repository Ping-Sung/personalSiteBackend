from django.urls import path

from . import views

# The followint three group of urls are for the same purpose, but using different views.
# The first group is using generic views, the second group is using function based views, and the third group is using mixins.
# documentation: https://www.django-rest-framework.org/api-guide/generic-views/
urlpatterns = [

    # generic view
    path('', views.DiaryListCreateApiView.as_view()),
    path('<int:pk>/', views.DiaryDetailApiView.as_view(), name='diary-detail'),
    path('<int:pk>/update/', views.DiaryUpdateApiView.as_view(), name='diary-update'),
    path('<int:pk>/delete/', views.DiaryDeleteApiView.as_view(), name='diary-delete'),
    # path('', views.DiaryListApiView.as_view()),


    # # function based view
    # path('function_create/', views.diary_create_view),
    # path('function_create/<int:pk>/', views.diary_create_view),

    # generic mixins view (combination of generic views, use for RESTful APIs)
    # all CRUD operations are done in the following minin views.
    path('mixins/', views.DiaryMixinApiView.as_view()),
    path('mixins/<int:pk>/', views.DiaryMixinApiView.as_view()),

]