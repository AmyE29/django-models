from django.db import models

# Create your models here.
class Flavor(models.Model):
    name = models.CharField(max_length= 100)
    description = models.TextField()
    author = models.ForeignKey('auth.User', on_delete = models.CASCADE)

    def __str__(self):
        return self.name
