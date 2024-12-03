from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager



class UserProfileManager(BaseUserManager):
    """Manager for User Profiles"""
    def create_user(self, email, name, password=None):
        """create new user profile"""
        if not email:
            raise ValueError('users must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """create new super user with admin rights"""
        user = create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = AbstractBaseUser
        user.save(using=self._db)

        return user

class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Get users full name"""
        return self.name

    def get_short_name(self):
        """Get users short name"""
        return self.name

    def __str__(self):
        """Return string representation of user"""
        return self.email
