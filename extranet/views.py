from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import CompanyCustomer

# Create your views here.

def index(request):
    customer_list = CompanyCustomer.objects.all()
    context = {'customer_list': customer_list}
    return render(request, 'extranet/index.html', context)