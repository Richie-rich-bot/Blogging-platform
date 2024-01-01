from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser,PermissionsMixin

class UserManager(BaseUserManager):
    def create_user(self,email,password = None, **extra_fields):
        """Create, save and return a new user"""
        if not email:
                raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email = email,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user
    def create_superuser(self,email, password= None):
         """Create and return a new superuser"""
         user = self.create_user(email, password)
         user.is_staff = True
         user.is_superuser = True
         user.save(using=self._db)
         return user

class User(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(max_length= 255, unique = True)
    name = models.CharField(max_length = 255)
    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = False)
    objects = UserManager()
    USERNAME_FIELD = 'email'