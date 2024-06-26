from django.db import models

class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Image(models.Model):
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.image.name

from django.db import models

class UploadedImage(models.Model):
    image = models.ImageField(upload_to='uploaded_images/')

