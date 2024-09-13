from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name = "home"),
    path("login/", views.login, name = "login"),
    path("user/", views.user_details, name="user_details"),
    path('add-kpi/', views.add_kpi, name='add_kpi'),
    path('delete/<int:kpi_id>/', views.delete_kpi, name='delete_kpi'),
]
