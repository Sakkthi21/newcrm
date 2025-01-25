from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),

    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerUser, name="register"),
    path('customerRecord/<str:pk>/', views.customerRecord, name="customer"),
    path('delete/<str:pk>/', views.deleteCustomer, name="delete"),
    path('add-record/', views.addRecord, name="add-record"),
    path('update/<str:pk>/', views.updateRecord, name="update"),
]
