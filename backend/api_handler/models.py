from django.db import models


# Create your models here.
class User(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=32)
    role = models.CharField(max_length=255)
    verified = models.BooleanField()
    provider = models.CharField(max_length=255)

    def __str__(self):
        return self.full_name

    def set_password(self, password):
        self.password = password
