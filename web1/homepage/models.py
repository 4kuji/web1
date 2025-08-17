from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
# Create your models here.


# class CustomUserManager(BaseUserManager):
#     def create_user(self, email, password=None, **extra_fields):
#         if not email:
#             raise ValueError("Users must have an email address")
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, email, password=None, **extra_fields):
#         extra_fields.setdefault("is_staff", True)
#         extra_fields.setdefault("is_superuser", True)
#         extra_fields.setdefault("is_active", True)
#         return self.create_user(email, password, **extra_fields)


# class Custom(AbstractUser):
#     first_name = models.CharField(max_length=30,blank=True)
#     last_name = models.CharField(max_length=30,blank=True)
#     email = models.EmailField(max_length=100,unique=True)
#     address = models.CharField(blank=True, max_length=300)
#     city = models.CharField(max_length=30,blank=True)
#     state = models.CharField(max_length=30,blank=True)
#     pin = models.IntegerField(blank=True,default=0)
   

#     USERNAME_FIELD ="email"
#     REQUIRED_FIELDS = []
#     objects = CustomUserManager()  # Manager burada!

#     def __str__(self):
#         return self.email

#     def create_superuser(self, email, password=None, **extra_fields):
#         if not email:
#             raise ValueError("User must have an email")
#         if not password:
#             raise ValueError("User must have a password")
        

#         user = self.model(
#             email=self.normalize_email(email)
#         )
#         USERNAME_FIELD ="email"
#         user.set_password(password)
#         user.admin = True
#         user.staff = True
#         user.active = True
#         user.save(using=self._db)
#         return user


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Users must have an email address")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        return self.create_user(email, password, **extra_fields)


class Custom(AbstractUser):
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    email = models.EmailField(max_length=100, unique=True)
    address = models.CharField(blank=True, max_length=300)
    city = models.CharField(max_length=30, blank=True)
    state = models.CharField(max_length=30, blank=True)
    pin = models.IntegerField(blank=True, default=0)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    
class Event(models.Model):
    title = models.CharField(max_length=200)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    


class Attendee(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    email = models.EmailField()


class Book(models.Model):
    require = models.CharField(max_length=200,null=True)
    description = models.TextField()
    start_time = models.DateField()
    end_time = models.TimeField()


