from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Permission, Group, User
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_user(self, phone_number, password=None, **extra_fields):
        if not phone_number:
            raise ValueError('Должен быть указан номер телефона')
        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, phone_number, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(phone_number, password, **extra_fields)
    

class CustomUser(AbstractBaseUser, PermissionsMixin):
    phone_number = models.CharField(max_length=15, unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []

    user_permissions = models.ManyToManyField(
        Permission,
        blank=True,
        related_name='permissions'  # Добавляем related_name
    )

    groups = models.ManyToManyField(
        Group, 
        blank=True,
        related_name='groups',
    )

    def __str__(self):
        return self.phone_number
    

class UserInfo(models.Model):
    user = models.OneToOneField(CustomUser, related_name='user_info', null=True, blank=True, on_delete=models.CASCADE)
    is_shelter_owner = models.BooleanField(default=False) # в зависимости от значения, некоторые поля должны быть null
    contacts = models.CharField(max_length=100, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True) # для частника ФИО
    rating = models.FloatField(null=True, blank=True)