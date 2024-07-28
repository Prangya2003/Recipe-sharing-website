from django.db import models
from django.contrib.auth import get_user_model
from userprofile.models import UserProfileModel
# Create your models here.

class RecipeModel(models.Model):
    chef = models.ForeignKey(get_user_model(),on_delete=models.CASCADE,related_name="RecipeModel_chef",null=True,blank=True)
    recipe_name = models.CharField(max_length=200)
    picture = models.ImageField(upload_to='recipes/',blank=True,null=True)
    cuisine = models.CharField(max_length=100, default='Unknown')
    time_to_cook = models.CharField(max_length=100,default=0)
    food_type = models.CharField(max_length=100,default='Unknown')
    description = models.TextField()
    ingredients = models.TextField(blank=True, null=True)
     
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return self.recipe_name
    

    def get_ratings(self):
        return self.ratingModel_recipe.all()
    
class CommentModel(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="CommentModel_user", null=True)
    recipe = models.ForeignKey('RecipeModel', on_delete=models.CASCADE, related_name="comments", null=True)
    comment = models.CharField(max_length=100, null=True, blank=True)  

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)

class RatingModel(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="RatingModel_user", null=True)
    recipe = models.ForeignKey('RecipeModel', on_delete=models.CASCADE, related_name="RatingModel_recipe", null=True)
    score = models.PositiveIntegerField()

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
     