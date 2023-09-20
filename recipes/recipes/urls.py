from django.urls import path
from calculator.views import recipe_view

urlpatterns = [
    path('<str:product>/', recipe_view, name='recipe')
]
