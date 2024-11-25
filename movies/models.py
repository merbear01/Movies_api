from django.db import models

# Create your models here.
class Movies(models.Model):
    title = models.CharField(max_length=100, blank=True, default='')
    overview = models.TextField(blank=True, default='')
    release_date = models.DateField(null=False, default='2000-01-01')
    poster_path = models.CharField(max_length=100, blank=True, default='')
    popularity = models.FloatField(default=0)
    vote_average = models.FloatField(default=0)
    vote_count = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']

