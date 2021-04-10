from django.db import models

# Create your models here.
class Userinfo(models.Model):
    uid = models.AutoField
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    query = models.CharField(max_length=150)

    def __str__(self):
        return self.query