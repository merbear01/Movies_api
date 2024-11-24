from django.db import models

# Create your models here.
class Movies(models.Model):
    title = models.CharField(max_length=100, blank=True, default='')
    overview = models.TextField(blank=True, default='')
    year=models.IntegerField()
    poster_path=models.CharField(max_length=100, blank=True, default='')
    genre=models.CharField(max_length=100, blank=True, default='')
    director=models.CharField(max_length=100, blank=True, default='')
    rating=models.FloatField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['rating']

