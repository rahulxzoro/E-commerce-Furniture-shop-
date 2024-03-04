from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages,auth
from django.contrib.auth import authenticate, login as auth_login

# Create your views here.
def register(request):
    if request.method=='POST':
        Username=request.POST['username']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        password=request.POST['password']
        c_password=request.POST['c_password']
        # customer_type=request.POST['customer_type',None ]
        if password==c_password:
            if User.objects.filter(username=Username).exists():
                messages.info(request,"username already taken")
                return redirect('credential:register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email id is already taken")
                return redirect('credential:register')
            else:
               
                user=User.objects.create_user(username=Username,first_name=first_name,last_name=last_name,email=email,password=password)
                user.save()
                return redirect('credential:login')
        else:
            messages.info(request,'Password does not matched')
            return redirect('register')
        
    return render(request,'register.html')       

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            if hasattr(user, 'id'):
                request.session['user'] = user.id
            return redirect('/')
        else:
            messages.error(request, "Invalid username or password")
            return redirect('credential:login')

    return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    request.session.flush()
    return redirect('/')