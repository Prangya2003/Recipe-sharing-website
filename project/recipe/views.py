from django.shortcuts import render,get_object_or_404,redirect
from .models import RecipeModel
from django.core.files.storage import default_storage
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
# Create your views here.

def recipe_detail(request,id):
    recipe = get_object_or_404(RecipeModel,id=id)
    
    # If recipes exist, get the creator's username for the first recipe
    creator_username = recipe.chef.username if recipe.chef else None
       
    
    context = {
        'recipe': recipe,
        'creator_username': creator_username
    }
    
    return render(request, 'recipe_detail.html', context)

def recipe_list(request):
    recipes = RecipeModel.objects.all()  # Fetch all recipes
    context = {
        'recipes': recipes
    }
    return render(request, 'recipe_list.html', context)


User = get_user_model()
@login_required
def create_recipe_view(request):
    if request.method == 'POST':
        recipe_name = request.POST.get('recipe_name')
        description = request.POST.get('description')
        picture = request.FILES.get('picture')

        chef = request.user if request.user.is_authenticated else User.objects.get(username='defaultuser')

        recipe = RecipeModel(
            recipe_name=recipe_name,
            description=description,
            picture=picture,
            chef=chef
        )
        recipe.save()

        return redirect('recipe_detail',id=recipe.id)  

    return render(request, 'create_recipe.html')

@login_required
def update_recipe_view(request,id):
    recipe = get_object_or_404(RecipeModel, id=id,chef=request.user) 
    if request.method == "POST":
        recipe.recipe_name = request.POST.get('recipe_name')
        if len(request.FILES) != 0:
            recipe.picture = request.FILES.get('picture')
        recipe.description = request.POST.get('description')
        recipe.save()
        return redirect('recipe_detail',id=recipe.id)     
    return render(request,'update_recipe.html', {'recipe':recipe})

@login_required
def delete_recipe_view(request, id):
    if request.method == 'POST':
        recipe = get_object_or_404(RecipeModel, id=id)
        if recipe.chef == request.user:
            recipe.delete()
            return redirect('profile_view', username=request.user.username)
        else:
            return render(request, 'error.html', {'message': 'You are not authorized to delete this post.'})