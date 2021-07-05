from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('admin/', views.admin, name='admin'),
    path('logout/', views.logout, name='logout'),
    path('edit/<int:district_id>', views.edit, name='edit')
]