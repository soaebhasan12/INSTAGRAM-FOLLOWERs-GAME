from django.db import models

# Create your models here.
class Upload(models.Model):
    image = models.ImageField(upload_to = "image/", null= False)
    name = models.CharField(max_length = 40, null = False)
    country = models.CharField(max_length = 40, null = False)
    description = models.CharField(max_length = 70, null = False)
    follower_count = models.IntegerField(null = False)

    def __str__(self):
        return f"{self.name}"