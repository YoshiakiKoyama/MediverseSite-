from django.db import models


class Beatmap(models.Model):
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    instrument = models.CharField(max_length=50)
    file_format = models.CharField(max_length=20)
    difficulty = models.IntegerField(default=1)

    file = models.FileField(upload_to='beatmaps/', null=True, blank=True)

    def __str__(self):
        return self.title