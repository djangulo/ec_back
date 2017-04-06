from django.db import models

def work_directory_path(instance, filename):
    return 'works_images/work_{}/{}'.format(instance.id, filename)

def publication_directory_path(instance, filename):
    return 'publication_images/pub_{}/{}'.format(instance.id, filename)    


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
    category = models.ForeignKey(
        Category,
        related_name="press_releases",
        on_delete=models.CASCADE
    )
    url = models.URLField()
    class Meta(Media.Meta):
        verbose_name = 'press release'
        verbose_name_plural = 'press releases'


class Work(Media):
    STATUS_CHOICES = (
        (0, 'Planned'),
        (1, 'Under Construction'),
        (2, 'Completed'),
    )
    category = models.ForeignKey(
        Category,
        related_name="works",
        on_delete=models.CASCADE
    )
    program = models.CharField(max_length=75)
    status = models.IntegerField(choices=STATUS_CHOICES)
    team = models.TextField(default='')
    date_released = models.DateField()
    class Meta(Media.Meta):
        verbose_name = 'work'
        verbose_name_plural = 'works'


class WorkPicture(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to=work_directory_path, blank=True, null=True)
    caption = models.TextField()
    work = models.ForeignKey(Work, related_name='pictures')
    is_cover = models.BooleanField(
        default=False,
        help_text="If yes, this image will be the cover of the 'Work' entry it belongs to."
    )

    def __str__(self):
        return 'Image: {} from Work: {}'.format(
            self.title,
            self.work.title
        )

class Publication(Media):
    TYPE_CHOICES = (
        (0, 'Article'),
        (1, 'Review'),
        (2, 'Book'),
        (3, 'Blogpost'),
    )
    type = models.IntegerField(choices=TYPE_CHOICES, default=0)
    category = models.ForeignKey(
        Category,
        related_name="publications",
        on_delete=models.CASCADE
    )
    image = models.ImageField(
        upload_to=publication_directory_path,
        blank=True,
        null=True
    )
    class Meta(Media.Meta):
        verbose_name = 'publication'
        verbose_name_plural = 'publications'



