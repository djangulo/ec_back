from django.db import models
from django.template.defaultfilters import slugify
from django.utils import timezone


def work_directory_path(instance, filename):
    IMAGE_FILE_FORMATS = [
        '.jpg', '.jpeg', '.jif', '.jfif',
        '.jp2', '.jpx', '.j2k', '.j2c',
        '.png',
        '.tiff', '.tif',
        '.svg',
        '.gif',
        '.pcd',
        '.bmp',
    ]
    for f in IMAGE_FILE_FORMATS:
        if filename.endswith(f):
            return 'works/images/work_{}/{}'.format(instance.id, filename)
    return 'works/files/work_{}/{}'.format(instance.id, filename)

def publication_directory_path(instance, filename):
    return 'publications/images/pub_{}/{}'.format(instance.id, filename)    


class Category(models.Model):
    name = models.CharField(max_length=50, blank=False)
    description = models.CharField(max_length=255, blank=True, default='')

    class Meta:
        verbose_name_plural = 'categories'
        ordering = ('name',)

    def __str__(self):
        return self.name


class PressRelease(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    category = models.ForeignKey(
        Category,
        related_name="press_releases",
        on_delete=models.CASCADE
    )
    url = models.URLField(blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    class Meta:
        verbose_name = 'press release'
        verbose_name_plural = 'press releases'

    def __str__(self):
        return self.title

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def unpublish(self):
        self.published_date = None
        self.save()

    @property
    def slug(self):
        return slugify(self.title)

class Work(models.Model):
    STATUS_CHOICES = (
        (0, 'Planned'),
        (1, 'Under Construction'),
        (2, 'Completed'),
    )
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255, blank=True)
    category = models.ForeignKey(
        Category,
        related_name="works",
        on_delete=models.CASCADE
    )
    program = models.CharField(max_length=75, blank=True)
    status = models.IntegerField(choices=STATUS_CHOICES)
    team = models.TextField(default='', blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    document = models.FileField(upload_to=work_directory_path, blank=True, null=True)
    class Meta:
        verbose_name = 'work'
        verbose_name_plural = 'works'

    def __str__(self):
        return self.title

    @property
    def slug(self):
        return slugify(self.title)


class WorkPicture(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to=work_directory_path, blank=True, null=True)
    caption = models.TextField(blank=True)
    work = models.ForeignKey(Work, related_name='pictures')
    is_cover = models.BooleanField(
        default=False,
        help_text="If yes, this image will be the cover of the 'Work' entry it belongs to."
    )

    def __str__(self):
        return 'Image: {} - {}'.format(
            self.title,
            self.work.title
        )

    @property
    def slug(self):
        return slugify(self.title)

class Publication(models.Model):
    ARTICLE = 0
    REVIEW = 1
    BOOK = 2
    BLOGPOST = 3
    MEDIUM_CHOICES = (
        (ARTICLE, 'Article'),
        (REVIEW, 'Review'),
        (BOOK, 'Book'),
        (BLOGPOST, 'Blogpost'),
    )
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255, blank=True)
    medium = models.IntegerField(choices=MEDIUM_CHOICES, default=ARTICLE)
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
    class Meta:
        verbose_name = 'publication'
        verbose_name_plural = 'publications'

    def __str__(self):
        return self.title

    @property
    def slug(self):
        return slugify(self.title)
