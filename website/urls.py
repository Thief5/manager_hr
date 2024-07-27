from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('detalii/<int:pk>', views.utilizator_detalii, name='detalii'),
    path('sterge_utilizator/<int:pk>', views.sterge_utilizator, name='sterge_utilizator'),
    path('adauga_user/', views.adauga_user, name='adauga_user'),
    path('modifica_utilizator/<int:pk>', views.modifica_utilizator, name='modifica_utilizator'),

    
    
]

