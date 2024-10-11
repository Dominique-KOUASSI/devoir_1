
from django.urls import path
from . import views
from .views import CustomerListView  # Assure-toi que la vue est correctement importée

urlpatterns = [
    path('', CustomerListView.as_view(), name='customer_list'),  # Utilise l'importation ici
]

