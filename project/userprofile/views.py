
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages

from django.contrib.auth import get_user_model,authenticate,login,logout
from .models import UserProfileModel
from recipe.models import RecipeModel

# Create your views here.
def front_view(request):
    return render(request,'front.html')

def profile_view(request, username):
    User = get_user_model()
    user_instance = get_object_or_404(User, username=username)
    
    user_recipes = RecipeModel.objects.filter(chef=user_instance) 

    data = {
        "is_user_profile": request.user == user_instance,  
        "recipes_count": user_recipes.count(), 
        "user_recipes": user_recipes,
    }

    return render(request, 'profile.html', context={"request": request, "user": user_instance, "data": data})


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
            return redirect('signup_view')
            
        else:
            user_instance = get_user_model().objects.create(username=username,first_name=first_name,last_name=last_name,email=email)
            user_instance.set_password(password)
            user_instance.save()
            UserProfileModel.objects.create(user=user_instance)
            messages.info(request,'Userprofile created successfully')
        if not error_flag:
            return redirect('login_view')
    return render(request, 'signup.html')

def update_user_profile(request):
    user_instance = request.user
    user_profile_instance, created = UserProfileModel.objects.get_or_create(user=user_instance)
    
    if request.method == 'POST':
        user_instance.first_name = request.POST.get('first_name')
        user_instance.last_name = request.POST.get('last_name')

        new_username = request.POST.get('username')
        if new_username and new_username != user_instance.username:
            if get_user_model().objects.filter(username=new_username).exists():
                print("Username already taken")
            else:
                user_instance.username = new_username

        user_profile_instance.bio = request.POST.get('bio')
        if 'profile_picture' in request.FILES:
            user_profile_instance.profile_picture = request.FILES['profile_picture']

        user_profile_instance.save()
        user_instance.save()

        return redirect('profile_view', username=user_instance.username)

    context = {"request": request, "user": user_instance, "profile": user_profile_instance}
    return render(request, 'update_userprofile.html', context)


def update_password_view(request):
    user_instance = request.user
    
    if request.method == 'POST':
        current_password = request.POST.get('password')
        new_password = request.POST.get('new_password')
        new_password_check = request.POST.get('new_password_check')

        user_check = authenticate(username=user_instance.username, password=current_password)
        if user_check is not None:
            if new_password == new_password_check:
                user_instance.set_password(new_password)
                user_instance.save()
                
                # Re-authenticate user to avoid logout after password change
                user = authenticate(username=user_instance.username, password=new_password)
                if user is not None:
                    login(request, user)
                
                return redirect('profile_view', username=user_instance.username)
            else:
                print("New passwords do not match")

    context = {"request": request, "user": user_instance}
    return render(request, 'update_password.html', context)


def logout_view(request):
    logout(request)
    return redirect('front_view')
    
def home_view(request):
    if request.user.is_authenticated:
        recipes = RecipeModel.objects.all()  # Fetch all recipes
        context = {
            'recipes': recipes
        }
        return render(request, 'home.html', context)
    else:
        return redirect('login_view')
 
def faq_view(request):
    return render(request, 'faq.html')

def contact_view(request):
    return render(request, 'contact.html')

def services_view(request):
    return render(request, 'services.html')