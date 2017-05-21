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
            return 'works/images/work_{}/{}'.format(instance.work_id, filename)
    return 'works/files/work_{}/{}'.format(instance.id, filename)

def publication_directory_path(instance, filename):
    return 'publications/images/publication_{}/{}'.format(instance.id, filename)

def press_directory_path(instance, filename):
    return 'press/kits/{}-{}/{}-{}'.format(
        instance.created_date.year,
        instance.created_date.month,
        instance.title,
        filename
    )


class Item(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, blank=False, default='')
    description = models.TextField(max_length=500, blank=True, default='')
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    display_order = models.IntegerField(default=0)

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

class PressDatesManager(models.Manager):
    def get_queryset(self):
        return super(
            PressDatesManager,
            self
        ).get_queryset().dates('published_date', 'month')


class Press(Item):
    category = models.ForeignKey(
        Category,
        related_name="presses",
        on_delete=models.CASCADE
    )
    url = models.URLField(blank=True, help_text="URL to external resource or additional info")
    press_kit = models.FileField(upload_to=press_directory_path, blank=True, null=True)

    objects = models.Manager()
    archive_dates = PressDatesManager()

    class Meta(Item.Meta):
        verbose_name = 'press release'
        verbose_name_plural = 'press releases'

    def get_year_month(self):
        return {
            'year': self.published_date.year,
            'month': self.published_date.month
        }


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
    url = models.URLField(blank=True, help_text="URL to external resource or additional info")
    class Meta(Item.Meta):
        verbose_name = 'publication'
        verbose_name_plural = 'publications'
