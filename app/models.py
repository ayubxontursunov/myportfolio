from django.db import models

class Comment(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    subject = models.CharField(max_length=100)
    text = models.CharField(max_length=500)


    def __str__(self):
        return self.name
