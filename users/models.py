from django.db import models

# Create your models here.
class User(models.Model):
    id= models.UUIDField(primary_key=True,)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField()

    def __str__(self):
        return self.name