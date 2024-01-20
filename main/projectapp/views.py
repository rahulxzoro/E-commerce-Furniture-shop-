from django.shortcuts import render,get_object_or_404
from . models import Category,Product
from django.core.paginator import Paginator,EmptyPage,InvalidPage

# Create your views here.
def home(request,c_slug=None):
    obj=Category.objects.all()
    c_page=None
    if c_slug!=None:
        c_page = get_object_or_404(Category, slug=c_slug)
        product_list = Product.objects.all().filter(category=c_page,available=True)
    else:    
        product_list=Product.objects.all().filter(available=True)

    paginator = Paginator(product_list,8) 
    try:
        page = int(request.GET.get('page'))
    except:
        page = 1
    try:
        products = paginator.page(page)
    except(EmptyPage,InvalidPage):
        products =paginator.page(paginator.num_pages)
    return render(request, 'index.html',{"category":obj,'product':c_page})

def category(request, id=None):
    if id is not None:
        # Fetch the specific category if id is provided
        data = get_object_or_404(Category, id=id)
        products = Product.objects.filter(category=data)
    else:
        # Fetch all products if id is not provided
        products = Product.objects.all()

    return render(request, 'category.html', {"products": products})

def details(request ,id):
    
    products = Product.objects.get(id=id)
    return render(request,'details.html',{'products':products})