from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('profile/', views.profile_view, name='profile'),
    path('submit-kpi/', views.kpi_submission, name='kpi_submission'),
    path('download-kpi/', views.download_kpi, name='download_kpi'),
    path('', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
