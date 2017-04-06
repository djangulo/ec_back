from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50, blank=False)
    description = models.CharField(max_length=255, blank=False)

    class Meta:
        verbose_name_plural = 'categories'
        ordering = ('name',)

    def __str__(self):
        return self.name


class Media(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    slug = models.SlugField()
    class Meta:
        abstract = True

    def __str__(self):
        return self.title


class PressRelease(Media):
    date_released = models.DateField()
    category = models.ForeignKey(Category, related_name="press_releases")
    class Meta(Media.Meta):
        verbose_name = 'press release'
        verbose_name_plural = 'press releases'


class Work(Media):
    STATUS_CHOICES = (
        (0, 'Planned'),
        (1, 'Under Construction'),
        (2, 'Completed'),
    )
    category = models.ForeignKey(Category, related_name="works")
    program = models.CharField(max_length=75)
    status = models.IntegerField(choices=STATUS_CHOICES)
    team = models.TextField(default='')
    class Meta(Media.Meta):
        verbose_name = 'work'
        verbose_name_plural = 'works'


class Publication(Media):
    TYPE_CHOICES = (
        (0, 'Article'),
        (1, 'Review'),
        (2, 'Book'),
        (3, 'Blogpost'),
    )
    type = models.IntegerField(choices=TYPE_CHOICES, default=0)
    category = models.ForeignKey(Category, related_name="publications")
    class Meta(Media.Meta):
        verbose_name = 'publication'
        verbose_name_plural = 'publications'


