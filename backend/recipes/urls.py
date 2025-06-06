from django.urls import path
from .views import (
    RecipeListCreateView, 
    RecipeDetailView, 
    BookmarkListCreateView, 
    BookmarkDeleteView,
    CategoryListCreateView,
    CategoryDetailView
)

urlpatterns = [
    path('', RecipeListCreateView.as_view(), name='recipe-list-create'),
    path('<int:pk>/', RecipeDetailView.as_view(), name='recipe-detail'),
    path('bookmarks/', BookmarkListCreateView.as_view(), name='bookmark-list-create'),
    path('bookmarks/<int:pk>/', BookmarkDeleteView.as_view(), name='bookmark-delete'),
    path('categories/', CategoryListCreateView.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
]
