from django.db import models

# Create your models here.

def home_image_directory_path(instance, filename):
    return 'home-images/{}'.format(filename)

class HomeImage(models.Model):
    title = models.CharField(max_length=100, blank=True, default='-')
    slug = models.SlugField(max_length=100, blank=True, default='')
    image = models.ImageField(upload_to=home_image_directory_path, blank=False, null=True)
    caption = models.TextField(blank=True)
    order = models.IntegerField(default=0, blank=True)
    
    class Meta:
        ordering = ('order',)
        verbose_name = 'home image'
        verbose_name_plural = 'home images'

    def __str__(self):
        return self.title