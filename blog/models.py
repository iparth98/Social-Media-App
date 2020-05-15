from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# from PIL import Image

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(default="default.jpg", upload_to="BlogPost-image")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})
        #
        # def save(self, *args, **kwargs):
        #     super(Post, self).save(*args, **kwargs)
        #
        #     img = Image.open(self.image.path)
        #
        #     if img.height > 300 or img.width > 600:
        #         output_size = (300, 600)
        #         img.thumbnail(output_size)
        #         img.save(self.image.path)
