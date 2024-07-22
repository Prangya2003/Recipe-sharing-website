from django.shortcuts import render,redirect
from django.contrib.auth import get_user_model,authenticate,login,logout
from .models import UserProfileModel
# Create your views here.
def front_view(request):
    return render(request,'front.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user_instance = authenticate(username=username, password=password)
        if user_instance is not None:
            login(request,user_instance)
            return redirect('home_view')
        else:
            print("Invalid username or password")
            return redirect('login_view')

    return render(request, 'login.html') 

def signup_view(request):
    error_flag = False  
    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')
        email = request.POST.get('email')

        if get_user_model().objects.filter(username=username).exists():
            # messages.error(request,"Username is already taken")
            error_flag = True

        else:
            user_instance = get_user_model().objects.create(username=username,first_name=first_name,last_name=last_name,email=email)
            user_instance.set_password(password)
            user_instance.save()
            UserProfileModel.objects.create(user=user_instance) 

        if not error_flag:
            return redirect('login_view')
    return render(request, 'signup.html')

def logout_view(request):
    logout(request)
    return redirect('front_view')
    
def home_view(request):
    if request.user.is_authenticated:
        return render(request,'home.html')
    else:
        return redirect('login_view')

def profile_view(request,username):
    user_instance = get_user_model().objects.get(username=username)
    data = {
        
    }
    return render(request, 'profile.html',context={"request":request,"user":user_instance,"data":data})
    
def faq_view(request):
    return render(request, 'faq.html')

def contact_view(request):
    return render(request, 'contact.html')

def services_view(request):
    return render(request, 'services.html')