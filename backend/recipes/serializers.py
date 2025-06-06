from rest_framework import serializers
from .models import Recipe, Bookmark, Category

class RecipeSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Recipe
        fields = '__all__'
        read_only_fields = ('author', 'created_at', 'updated_at')


class BookmarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookmark
        fields = ['id', 'user', 'recipe', 'external_id', 'title', 'thumbnail']
        read_only_fields = ['user']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']
        