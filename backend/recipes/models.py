from django.db import models
from django.conf import settings

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    title = models.CharField(max_length=255)
    ingredients = models.TextField()
    instructions = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='recipe_images/', blank=True, null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='recipes')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='recipes')

    def __str__(self):
        return self.title

class Bookmark(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    recipe = models.ForeignKey('Recipe', on_delete=models.CASCADE, null=True, blank=True)
    external_id = models.CharField(max_length=100, null=True, blank=True)
    title = models.CharField(max_length=255)
    thumbnail = models.URLField(blank=True)

    class Meta:
        unique_together = ('user', 'recipe', 'external_id')

    def __str__(self):
        return f'{self.user.username} bookmarked {self.title}'
