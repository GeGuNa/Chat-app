from . import views
from django.urls import path

urlpatterns = [
    #path('', views.main, name="main"),
    path('file/', views.kz_file, name="kz_file"),
    path('file/<str:test>/', views.main_test, name="main_test"),
    path('xz/', views.main_test2, name="main_test2"),
    path('session/', views.main_of_session, name="main_of_session"),
    path('', views.Main_pg2, name="Main_pg2")
]
