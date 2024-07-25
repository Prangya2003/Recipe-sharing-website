from django.db import models

# Create your models here.
from django.contrib.auth import get_user_model


class UserProfileModel(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, related_name="profile", null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    saved_recipes = models.ManyToManyField('recipe.RecipeModel', related_name='saved_by_users', blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return self.user.username
    
    
    
    