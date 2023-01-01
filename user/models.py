from django.db import models
from django.contrib.auth.models import AbstractUser
from shared.choices import USER_ROLE


# Create your models here.

class User(AbstractUser):
    first_name = models.CharField(max_length=150, blank=False)
    last_name = models.CharField(max_length=150, blank=False)
    user_role = models.CharField(max_length=25, choices=USER_ROLE, default="CUSTOMER")
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128, blank=False)

    def save(self, *args, **kwargs):
        self.full_clean()
        super(User, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        super(User, self).delete(*args, **kwargs)






