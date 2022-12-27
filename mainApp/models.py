from django.db import models

# Create your models here.
class count(models.Model):
    likeCount = models.IntegerField(default=0)
    dislikeCount = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.likeCount}'