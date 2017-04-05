from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50, blank=False)
    description = models.CharField(max_length=255, blank=False)

    class Meta:
        verbose_name_plural = 'categories'
        ordering = ('name',)


class Media(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    slug = models.SlugField()
    class Meta:
        abstract = True


class PressRelease(Media):
    date_released = models.DateField()
    category = models.ForeignKey(Category, related_name="press_releases")
    class Meta:
        verbose_name = 'press release'
        verbose_name_plural = 'press releases'


class Work(Media):
    STATUS_CHOICES = (
        (0, 'planned'),
        (1, 'under_construction'),
        (2, 'completed'),
    )
    category = models.ForeignKey(Category, related_name="works")
    program = models.CharField(max_length=75)
    status = models.IntegerField(choices=STATUS_CHOICES)
    team = models.TextField(default='')
    class Meta:
        verbose_name = 'work'
        verbose_name_plural = 'works'


class Publication(Media):
    TYPE_CHOICES = (
        (0, 'article'),
        (1, 'review'),
        (2, 'book'),
        (3, 'blogpost'),
    )
    type = models.IntegerField(choices=TYPE_CHOICES, default=0)
    category = models.ForeignKey(Category, related_name="publications")
    class Meta:
        verbose_name = 'publication'
        verbose_name_plural = 'publications'


