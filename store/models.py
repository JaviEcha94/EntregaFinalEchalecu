from django.db import models

class Game(models.Model):
    title = models.CharField(max_length=100)
    year = models.IntegerField()
    genre = models.CharField(max_length=50)
    rating = models.CharField(max_length=10, help_text="Ej: E, T, M, R")
    cover = models.ImageField(upload_to='covers/', null=True, blank=True)

    def __str__(self):
        return f"{self.title} ({self.year})"
