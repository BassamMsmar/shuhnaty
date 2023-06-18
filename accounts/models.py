from django.db import models
from django.contrib.auth.admin import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.
class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        if not username:
            raise ValueError("Users must have an email username")

        user = self.model(
            email = self.normalize_email(email),
            username = username
        )

        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, username, password):
        user = self.model(
                    email = self.normalize_email(email),
                    password = password,
                    username = username
                )

        user.is_admin= True
        user.is_staff= True
        user.is_superuser = True
        user.save(using=self._db)
        return user
            


class Account(AbstractBaseUser):
    pass

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Job_title  = models.CharField(max_length=100, blank=True, null=True)


    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
