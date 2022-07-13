from django.db import models

# Create your models here.


class Gallery(models.Model):

    class Meta:
        verbose_name_plural = "Gallery Images"

    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    caption = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name
