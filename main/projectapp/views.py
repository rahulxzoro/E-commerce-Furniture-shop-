from django.shortcuts import render,get_object_or_404,redirect
from . models import Category,Product,Details
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
    return render(request, 'index.html',{'category':obj,'product':c_page})

def category(request, id=None):
    data=None
    if id is not None:
        # Fetch the specific category if id is provided
        data = get_object_or_404(Category, id=id)
        products = Product.objects.filter(category=data)
    else:
        # Fetch all products if id is not provided
        products = Product.objects.all()

    return render(request, 'category.html', {"products": products,'data':data})

def details(request ,id):
    
    products = Product.objects.get(id=id)
    return render(request,'details.html',{'products':products})

def consult(request):
    
    return render(request,'consult.html')

def profile(request):   
    detail=Details.objects.all()
    return render(request,'profile.html',{'data': detail})

def address(request):
     detail=None
     if request.method == 'POST':
        address = request.POST.get('address')
        pincode = request.POST.get('pincode')
        city = request.POST.get('city')
        country = request.POST.get('country')
        phone = request.POST.get('phone')
        print(address,pincode,city,country,phone)
        detail=Details(address=address, pincode=pincode, city=city, country=country, phone=phone)
        detail.save()
        return redirect('furniture:profile')
     return render(request,'address.html',{'data':detail})
 
def edit(request,id):
    detail=Details.objects.get(id=id)
    if request.method == 'POST':
       address = request.POST.get('address')
       pincode = request.POST.get('pincode')
       city = request.POST.get('city')
       country = request.POST.get('country')
       phone = request.POST.get('phone')
       Details.objects.filter(id=id).update(address=address, pincode=pincode, city=city, country=country, phone=phone)
       return redirect('furniture:profile')
    return render(request,'edit.html',{'detail':detail})

def delete(request,id):

        details=Details.objects.get(id=id)
        details.delete()
        return redirect('furniture:profile')

def store(request):
    
    return render(request,'store.html')    


