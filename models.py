from django.db import models

class Application(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    grade = models.CharField(max_length=10)
    parent = models.CharField(max_length=100)
    motivation = models.TextField()

    def __str__(self):
        return self.name
