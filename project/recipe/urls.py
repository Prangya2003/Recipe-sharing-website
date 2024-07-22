from django.urls import path
#from .views import recipe_list,recipe_detail,create_recipe_view,update_recipe_view,delete_recipe_view
from .views import create_recipe_view,delete_recipe_view,update_recipe_view
urlpatterns = [
    #path('', recipe_list, name='recipe_list'),
    #path('recipe-detail/<int:id>/',recipe_detail, name='recipe_detail'),
    path('create-recipe/',create_recipe_view, name='create_recipe_view'),
    path('update-recipe/<int:id>/', update_recipe_view, name='update_recipe_view'),
    path('delete-recipe/<int:id>/', delete_recipe_view, name='delete_recipe_view'),
]
