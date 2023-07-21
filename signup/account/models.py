from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # Add any additional fields you want for your user model
    # For example, you can add a field for the user's email or profile picture
    email = models.EmailField(unique=True)

    # You can add more fields as per your requirements

    # Add this line to set a custom related_name for the groups ManyToManyField
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',  # You can choose any unique name you prefer
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )

    # Add this line to set a custom related_name for the user_permissions ManyToManyField
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_set',  # You can choose any unique name you prefer
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    def __str__(self):
        return self.username
