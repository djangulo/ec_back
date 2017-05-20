from django.conf import settings
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    Permission,
    PermissionsMixin
)
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

from rest_framework.authtoken.models import Token

@receiver(post_save, sender="accounts.User")
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        if instance.is_superuser:
            Token.objects.create(user=instance)

def user_directory_path(instance, filename):
    return 'user_photos/user_{}/{}'.format(
        instance.username,
        filename
    )

class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password, **extra_fields):
        if not username:
            raise ValueError('The given username must be set')
        email = self.normalize_email(email)
        username = self.model.normalize_username(username)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
        
    def create_superuser(self, username, email, password, **extra_fields):
        user = self.create_user(username=username, email=email, password=password)
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    NEITHER = 0
    STAFF = 1
    INTERN = 2
    BOTH = 3
    STAFF_INTERN_CHOICES = (
        (NEITHER, 'Neither'),
        (STAFF, 'Staff'),
        (INTERN, 'Intern'),
        (BOTH, 'Both')
    )
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(blank=True)
    first_name = models.CharField(max_length=50, blank=True, default='')
    last_name = models.CharField(max_length=50, blank=True, default='')
    photo = models.ImageField(upload_to=user_directory_path, blank=True, null=True)
    bio = models.TextField(default='', blank=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    staff_or_intern = models.IntegerField(
        choices=STAFF_INTERN_CHOICES,
        default=NEITHER,
        verbose_name="Is staff, intern or both?"
    )
    display_order = models.IntegerField(default=0)
    linkedin = models.URLField(default='', blank=True)
    facebook = models.URLField(default='', blank=True)
    instagram = models.URLField(default='', blank=True)


    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    class Meta:
        ordering = ('display_order', 'last_name', 'first_name',)

    def get_full_name(self):
        return '{} {} <{}>'.format(
            self.first_name,
            self.last_name,
            self.username
        )

    def get_short_name(self):
        return '{} ({})'.format(
            self.username,
            self.email
        )

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
    
    @property
    def is_superuser(self):
        return self.is_admin
