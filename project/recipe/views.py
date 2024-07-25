from django.shortcuts import render,get_object_or_404,redirect
from .models import RecipeModel
from django.core.files.storage import default_storage
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib import messages
from .models import RecipeModel
from userprofile.models import UserProfileModel
# Create your views here.

def recipe_detail(request,id):
    recipe = get_object_or_404(RecipeModel,id=id)
    creator_username = recipe.chef.username if recipe.chef else None   
    context = {
        'recipe': recipe,
        'creator_username': creator_username
    }
    
    return render(request, 'recipe_detail.html', context)

User = get_user_model()
@login_required
def create_recipe_view(request):
    if request.method == 'POST':
        recipe_name = request.POST.get('recipe_name')
        description = request.POST.get('description')
        picture = request.FILES.get('picture')
        cuisine = request.POST.get('cuisine')
        time_to_cook = request.POST.get('time_to_cook')
        food_type = request.POST.get('food_type')
        ingredients = request.POST.get('ingredients')
        chef = request.user if request.user.is_authenticated else User.objects.get(username='defaultuser')

        recipe = RecipeModel(
            recipe_name=recipe_name,
            description=description,
            picture=picture,
            chef=chef,
            cuisine=cuisine,
            time_to_cook=time_to_cook,
            food_type=food_type,
            ingredients=ingredients,
        )
        recipe.save()
        return redirect('recipe_detail',id=recipe.id)  
    return render(request, 'create_recipe.html')

@login_required
def update_recipe_view(request, id):
    recipe = get_object_or_404(RecipeModel, id=id)

    # Authorization check
    if recipe.chef != request.user:
        return render(request, 'error.html', {'message': 'You are not authorized to update this recipe.'})

    if request.method == "POST":
        recipe.recipe_name = request.POST.get('recipe_name')
        if 'picture' in request.FILES:
            recipe.picture = request.FILES.get('picture')
        recipe.description = request.POST.get('description')
        recipe.cuisine = request.POST.get('cuisine')
        recipe.time_to_cook = request.POST.get('time_to_cook')
        recipe.food_type = request.POST.get('food_type')
        recipe.ingredients = request.POST.get('ingredients')
        recipe.save()
        return redirect('recipe_detail', id=recipe.id)

    return render(request, 'update_recipe.html', {'recipe': recipe})

@login_required
def delete_recipe_view(request, id):
    recipe = get_object_or_404(RecipeModel, id=id)

    # Authorization check
    if recipe.chef != request.user:
        return render(request, 'error.html', {'message': 'You are not authorized to delete this recipe.'})

    if request.method == 'POST':
        recipe.delete()
        return redirect('profile_view', username=request.user.username)


    return render(request, 'confirm_delete.html', {'recipe': recipe})

#def review_view(request, id):

@login_required
def save_view(request, id):
    recipe = get_object_or_404(RecipeModel, id=id)

    if request.method == 'POST':
        # Get or create the UserProfileModel instance
        user_profile.created = UserProfileModel.objects.get_or_create(user=request.user)

        # Check if the recipe is already saved
        if recipe not in user_profile.saved_recipes.all():
            user_profile.saved_recipes.add(recipe)
            messages.success(request, "Recipe saved successfully.")
        else:
            messages.info(request, "This recipe is already saved.")

        # Redirect to the recipe detail page
        return redirect('recipe_detail', id=recipe.id)

    # If the request method is not POST, redirect to the recipe detail page
    return redirect('recipe_detail', id=recipe.id)

