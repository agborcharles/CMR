from django.shortcuts import render

# Create your views here.
def home(request):
    template_name = 'Bakery/dashboard.html'
    context = {}
    return render(request, template_name, context)

def categories(request):
    template_name = 'Bakery/categories.html'
    context = {}
    return render(request, template_name, context)

def products(request):
    template_name = 'Bakery/products.html'
    context = {}
    return render(request, template_name, context)


def suppliers(request):
    template_name = 'Bakery/suppliers.html'
    context = {}
    return render(request, template_name, context)

def customers(request):
    template_name = 'Bakery/customers.html'
    context = {}
    return render(request, template_name, context)

def orders(request):
    template_name = 'Bakery/orders.html'
    context = {}
    return render(request, template_name, context)
