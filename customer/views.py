
from django.shortcuts import render

from django.views.generic import ListView
from .models import Customer_info

def customer_list(request):
    # Your code here
    return render(request, 'customer_list.html')


class CustomerListView(ListView):
    model = Customer_info
    template_name = 'customer/customer_list.html'  # Chemin vers le template
    context_object_name = 'customer'  # Le nom utilisé dans le template
