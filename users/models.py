from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class UserRoles(models.Model):
    user_role = models.CharField(max_length=20)

    def __str__(self):
        return self.user_role

    class Meta:
        verbose_name_plural = 'User Roles'


class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15)
    role = models.ForeignKey(UserRoles, on_delete=models.CASCADE, null=True, blank=True)
    avatar = models.ImageField(upload_to='avatars/', default='avatars/default.png')

    def __str__(self):
        return str(self.username)
