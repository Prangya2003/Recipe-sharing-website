from django.urls import path
from .views import create_recipe_view,delete_recipe_view,update_recipe_view,recipe_detail
urlpatterns = [
    path('recipe-detail/<int:id>',recipe_detail, name='recipe_detail'),
    path('create-recipe/',create_recipe_view, name='create_recipe_view'),
    path('update-recipe/<int:id>/', update_recipe_view, name='update_recipe_view'),
    path('delete-recipe/<int:id>/', delete_recipe_view, name='delete_recipe_view'),
    
]
