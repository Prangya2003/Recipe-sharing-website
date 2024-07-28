
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from django.contrib.auth import get_user_model,authenticate,login,logout
from .models import UserProfileModel
from recipe.models import RecipeModel,CommentModel, RatingModel
from django.contrib.auth.decorators import login_required
from django.db.models import Q

# Create your views here.
def front_view(request):
    return render(request,'front.html')

@login_required
def profile_view(request, username):
    User = get_user_model()
    user_instance = get_object_or_404(User, username=username)

    # Fetch user profile
    user_profile = get_object_or_404(UserProfileModel, user=user_instance)

    # Fetch recipes by the user
    user_recipes = RecipeModel.objects.filter(chef=user_instance)
    
    data = {
        "is_user_profile": request.user == user_instance,
        "recipes_count": user_recipes.count(),
        "user_recipes": user_recipes,
        "user_profile": user_profile,
        "saved_recipes": user_profile.saved_recipes.all(),
    }
    
    context = {
        "request": request,
        "user": user_instance,
        "data": data
    }
    
    return render(request, 'profile.html', context)

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
            messages.success(request, "Invalid username or password")
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
            messages.error(request,"Username is already taken")
            error_flag = True
            return redirect('signup_view')
            
        else:
            user_instance = get_user_model().objects.create(username=username,first_name=first_name,last_name=last_name,email=email)
            user_instance.set_password(password)
            user_instance.save()
            UserProfileModel.objects.create(user=user_instance)
            messages.info(request,'Userprofile created successfully')
            messages.success(request,'Userprofile created successfully')
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

       
        if 'profile_picture' in request.FILES:
            user_profile_instance.profile_picture = request.FILES['profile_picture']

        user_profile_instance.save()
        user_instance.save()

        return redirect('profile_view', username=user_instance.username)

    context = {"request": request, "user": user_instance, "profile": user_profile_instance}
    return render(request, 'update_userprofile.html', context)


from django.contrib.auth import update_session_auth_hash
from django.contrib import messages

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
                    update_session_auth_hash(request, user)  # Update session to prevent logout
                    messages.success(request, 'Your password was successfully updated!')
                    return redirect('profile_view', username=user_instance.username)
                else:
                    messages.error(request, 'Authentication failed after password change.')
            else:
                messages.error(request, 'New passwords do not match.')
        else:
            messages.error(request, 'Current password is incorrect.')

    context = {"request": request, "user": user_instance}
    return render(request, 'update_password.html', context)


def logout_view(request):
    logout(request)
    return redirect('front_view')
 
@login_required
def delete_account_view(request):
    user_instance = request.user
    user_profile = get_object_or_404(UserProfileModel, user=user_instance)

    if request.method == 'POST':
        # Additional checks can be added here
        user_profile.delete()
        user_instance.delete()
        messages.success(request, 'Your account has been deleted successfully.')
        return redirect('front_view')

    return render(request, 'delete_account.html')

    
def home_view(request):
    if request.user.is_authenticated:
        recipes = RecipeModel.objects.all()
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

def search_profile_view(request):
    query = request.GET['query']
    recipesName = RecipeModel.objects.filter(recipe_name__icontains=query)
    recipesdescription = RecipeModel.objects.filter(description__icontains=query)
    recipescuisine = RecipeModel.objects.filter(cuisine__icontains=query)
    recipesfood_type = RecipeModel.objects.filter(food_type__icontains=query)
    recipestime_to_cook = RecipeModel.objects.filter(time_to_cook__icontains=query)


    recipes = recipesName.union(recipesdescription,recipescuisine,recipesfood_type,recipestime_to_cook)
    context = {
            'recipes': recipes,
            'query':query
        }

    return render(request, 'searching.html', context)

from django.http import HttpResponseRedirect

@login_required
def saved_recipes_view(request):
    print("Entered saved_recipes_view")
    user_profile = get_object_or_404(UserProfileModel, user=request.user)
    saved_recipes = user_profile.saved_recipes.all()
    
    if request.method == 'POST':
        recipe_id = request.POST.get('recipe_id')
        recipe = get_object_or_404(RecipeModel, id=recipe_id)
        
        if user_profile.saved_recipes.filter(id=recipe_id).exists():
            user_profile.saved_recipes.remove(recipe)
            messages.warning(request, "Recipe unsaved successfully")
        else:
            user_profile.saved_recipes.add(recipe)
            messages.success(request, "Recipe saved successfully")
        
        user_profile.save()
        
        return redirect(request.META.get('HTTP_REFERER', '/'))
    
    return render(request, 'userprofile/saved.html', {'saved_recipes': saved_recipes})