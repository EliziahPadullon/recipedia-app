from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.core.files.images import get_image_dimensions
from django.db import models

import os

def validate_image(image):

    max_size = 2 * 1024 * 1024
    if image.size > max_size:
        raise ValidationError("Image file size must be under 2MB.")


    valid_extensions = ['jpg', 'jpeg', 'png', 'webp']
    ext = os.path.splitext(image.name)[1][1:].lower()
    if ext not in valid_extensions:
        raise ValidationError("Unsupported file extension. Use JPG, PNG, or WebP.")

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(
        upload_to='profile_pics/',
        blank=True,
        null=True,
        validators=[validate_image]
    )

    def __str__(self):
        return self.username
