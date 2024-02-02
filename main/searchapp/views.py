from django.shortcuts import render
from projectapp.models import Product
from django.db.models import Q

# Create your views here.
def search(request):
    products=None
    query=None
    if 'q' in request.GET:
        query=request.GET.get('q')
        products=Product.objects.all().filter(Q(name__contains=query))
    return render(request,'search.html',{'query':query,'products':products})