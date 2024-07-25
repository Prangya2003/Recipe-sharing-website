from django.db import models
from django.contrib.auth import get_user_model
#from userprofile.models import UserProfileModel
# Create your models here.

class RecipeModel(models.Model):
    chef = models.ForeignKey(get_user_model(),on_delete=models.CASCADE,related_name="RecipeModel_chef",null=True,blank=True)
    recipe_name = models.CharField(max_length=200)
    picture = models.ImageField(upload_to='recipes/',blank=True,null=True)
    #rating = models.FloatField(default=0.0)
    cuisine = models.CharField(max_length=100, default='Unknown')
    time_to_cook = models.CharField(max_length=100,default=0)
    food_type = models.CharField(max_length=100,default='Unknown')
    description = models.TextField()
     
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    
    def __str__(self):
        return self.recipe_name
   
#class SavedRecipeModel(models.Model):
 ##   user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='saved_recipes')
   # saved_recipes = models.ManyToManyField(RecipeModel, related_name='saved_by_users')

   # updated_at = models.DateTimeField(auto_now=True)
    #created_at = models.DateTimeField(auto_now_add=True, editable=False)
#
    #def __str__(self):
    #    return self.user.username
