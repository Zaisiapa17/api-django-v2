from django.db import models

# Create your models here.
class Admin(models.Model):
    username = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    password = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username