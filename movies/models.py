from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    movie_id = models.CharField(max_length=50, unique=True)  # Foydalanuvchi shu ID ni kiritadi
    file_id = models.CharField(max_length=255, unique=True)  # Telegram’dan olingan fayl ID

    def __str__(self):
        return self.title
