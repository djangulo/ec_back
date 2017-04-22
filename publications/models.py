from django.db import models
from django.utils import timezone

from .support_models import Category, Medium, Program, Status

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
    for file_format in IMAGE_FILE_FORMATS:
        if filename.endswith(file_format):
            return 'works/images/work_{}/{}'.format(instance.id, filename)
    return 'works/files/work_{}/{}'.format(instance.id, filename)

def publication_directory_path(instance, filename):
    return 'publications/images/pub_{}/{}'.format(instance.id, filename)


class Item(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, blank=False, default='')
    description = models.TextField(max_length=500, blank=True, default='')
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def unpublish(self):
        self.published_date = None
        self.save()

    def _is_published(self):
        if self.published_date is not None:
            return True
        return False
    _is_published.boolean = True
    is_published = property(_is_published)


class Press(Item):
    category = models.ForeignKey(
        Category,
        related_name="presses",
        on_delete=models.CASCADE
    )
    url = models.URLField(blank=True, help_text="URL to external resource or additional info")

    class Meta(Item.Meta):
        verbose_name = 'press release'
        verbose_name_plural = 'press releases'


class Work(Item):
    """
    team: Leave as Text in case of collaborations with external companies
    Change to ManyToManyField after consulting with owner
    """
    category = models.ForeignKey(
        Category,
        related_name="works",
        on_delete=models.CASCADE
    )
    program = models.ForeignKey(
        Program,
        related_name="works",
        on_delete=models.CASCADE
    )
    status = models.ForeignKey(
        Status,
        related_name="works",
        on_delete=models.CASCADE
    )
    team = models.TextField(default='', blank=True)
    document = models.FileField(upload_to=work_directory_path, blank=True, null=True)
    class Meta(Item.Meta):
        verbose_name = 'work'
        verbose_name_plural = 'works'
        

class WorkPicture(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, blank=False, default='')
    image = models.ImageField(upload_to=work_directory_path, blank=True, null=True)
    caption = models.TextField(blank=True)
    work = models.ForeignKey(
        Work,
        related_name='pictures',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    def __str__(self):
        return 'Image of {} - {}'.format(
            self.work.title,
            self.title
        )
        
class WorkCover(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, blank=False, default='')
    image = models.ImageField(upload_to=work_directory_path, blank=True, null=True)
    caption = models.TextField(blank=True)
    work = models.OneToOneField(
        Work,
        related_name='cover',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    
    
    class Meta:
        verbose_name = 'cover'
        verbose_name_plural = 'cover'
    
    def __str__(self):
        return 'Cover Image of {}: {}'.format(
            self.work.title,
            self.title
        )


class Publication(Item):
    medium = models.ForeignKey(
        Medium,
        related_name="publications",
        on_delete=models.CASCADE
    )
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
    class Meta(Item.Meta):
        verbose_name = 'publication'
        verbose_name_plural = 'publications'
