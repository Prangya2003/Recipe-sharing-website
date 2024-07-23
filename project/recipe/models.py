from django.db import models
from django.contrib.auth import get_user_model
from userprofile.models import UserProfileModel
# Create your models here.

class RecipeModel(models.Model):
    chef = models.ForeignKey(get_user_model(),on_delete=models.CASCADE,related_name="RecipeModel_chef",null=True,blank=True)
    recipe_name = models.CharField(max_length=200)
    picture = models.ImageField(upload_to='recipes/',blank=True,null=True)
    description = models.TextField()
     
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    
    
    
     