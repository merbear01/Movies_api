from django.db import models

# Create your models here.
class Movies(models.Model):
    title = models.CharField(max_length=100, blank=True, default='')
    year=models.IntegerField()
    genre=models.CharField(max_length=100, blank=True, default='')
    director=models.CharField(max_length=100, blank=True, default='')
    rating=models.FloatField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['rating']

