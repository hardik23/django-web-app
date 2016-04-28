from django.db import models

# Create your models here.

class my_works(models.Model):
    title = models.CharField(max_length = 100)
    def __str__(self):
        return self.title
    class meta:
        ordering=["name"]




