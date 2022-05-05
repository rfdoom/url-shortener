from django.db import models

# Create your models here.
class URL(models.Model):
    longURL = models.CharField(max_length=255)
    shortURL = models.CharField(max_length=255)
    nickname = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.nickname