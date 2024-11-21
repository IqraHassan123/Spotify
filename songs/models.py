from django.db import models
from accounts.models import User
from accounts.models import UUIDModel

class Category(UUIDModel):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class Songs(UUIDModel):
    title=models.CharField(max_length=100)
    category=models.ForeignKey(Category, on_delete=models.CASCADE,default=None)
    artist=models.CharField(max_length=100)
    album=models.CharField(max_length=100)
    duration=models.DurationField()
    is_active=models.BooleanField(default=False)
    audio=models.FileField(upload_to='audio/')
    audio_image=models.ImageField(upload_to='audio_img/')

    def __str__(self):
        return self.title


class Playlist(UUIDModel):
    title=models.CharField(max_length=100)
    song=models.ManyToManyField(Songs, related_name='playlist')
    is_active=models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Download(UUIDModel):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    song=models.ForeignKey(Songs, on_delete=models.CASCADE,related_name='download')
    download_date = models.DateTimeField(auto_now_add=True)
    quality = models.CharField(max_length=10, choices=(('low', 'Low'), ('medium', 'Medium'), ('high', 'High')))

    def __str__(self):
        return f"{self.user.username} downloaded {self.song.title}"


