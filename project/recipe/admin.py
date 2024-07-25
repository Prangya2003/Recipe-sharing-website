from django.contrib import admin
from .models import RecipeModel,CommentModel,RatingModel

# Register your models here.
admin.site.register(RecipeModel)
admin.site.register(CommentModel)
admin.site.register(RatingModel)