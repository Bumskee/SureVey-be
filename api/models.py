from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)

class UserManager(BaseUserManager):
    def create_user(self, email, image, password=None, **extra_fields):
        if not email and image:
            raise ValueError('Please fill all forms and details.')

        user = self.model(
            email=self.normalize_email(email),
            image=image,
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self.db)
        return user
    
    def create_staffuser(self, email, password):
        user = self.create_user(
            email,
            password = password,
        )
        user.staff = True
        user.save(using=self.db)
        return user

    def create_superuser(self, email, image, password):
        user = self.create_user(
            email,
            image=image,
            password=password,
        )
        user.staff = True
        user.admin = True
        user.save(using=self.db)
        return user

# Create your models here.
class User(AbstractBaseUser):

    email = models.EmailField(
        verbose_name = 'email address',
        max_length=255,
        unique=True,
    )
    image = models.CharField(max_length=900000)
    staff = models.BooleanField(default=False) # for admin but not superuser
    admin = models.BooleanField(default=False) # for superuser

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['image'] # no need to put anything as username and password is required by default

    def get_full_name(self):
        return self.email
    
    def get_short_name(self):
        return self.email

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    objects = UserManager()

class Documents(models.Model):
    DocumentID = models.CharField(max_length=1000)
    DocumentName = models.CharField(max_length=500)
    DocumentDesc = models.TextField()
    DocumentQuests = models.JSONField()
    Creator = models.EmailField(
        verbose_name = 'email address',
        max_length=255,
    )