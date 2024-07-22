from django.shortcuts import render,get_object_or_404,redirect
from .models import RecipeModel
# Create your views here.

#def recipe_list(request):
#    recipes = RecipeModel.objects.all()
#    return render(request, 'recipe_list.html', {'recipes': recipes})

#def recipe_detail(request):
#    recipe = RecipeModel.objects.all()
#    return render(request,'recipe_detail.html',{'recipe':recipe})

def create_recipe_view(request):
    if request.method == 'POST':
        RecipeModel.objects.create(
            recipe_name = request.POST.get('recipe_name'),
            picture = request.FILES.get('picture'),
            description = request.POST.get('description'),
        )
    
        return redirect('create_recipe_view')
    
    recipes = RecipeModel.objects.all()
    context = {'recipes':recipes}
    return render(request, 'create_recipe.html',context)

def update_recipe_view(request,id):
    recipe = get_object_or_404(RecipeModel, id=id) 
    if request.method == "POST":
        recipe.recipe_name = request.POST.get('recipe_name')
        if len(request.FILES) != 0:
            recipe.picture = request.FILES.get('picture')
        recipe.description = request.POST.get('description')
        recipe.save()
        return redirect('create_recipe_view')     
    return render(request,'update_recipe.html', {'recipe':recipe})

def delete_recipe_view(request,id):
    recipe = get_object_or_404(RecipeModel, id=id)
    recipe.delete()
    return redirect('create_recipe_view')
    