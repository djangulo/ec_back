from django.db import models
from django.db.models import Count
from django.shortcuts import get_object_or_404
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
    for file_format in IMAGE_FILE_FORMATS:
        if filename.endswith(file_format):
            return 'works/images/work_{}/{}'.format(instance.id, filename)
    return 'works/files/work_{}/{}'.format(instance.id, filename)

def publication_directory_path(instance, filename):
    return 'publications/images/pub_{}/{}'.format(instance.id, filename)


class WorksCategoryManager(models.Manager):
    def get_queryset(self):
        return super(
            WorksCategoryManager,
            self
        ).get_queryset().filter(works__isnull=False).distinct()

         
class PublicationCategoryManager(models.Manager):
    def get_queryset(self):
        return super(
            PublicationCategoryManager,
            self
        ).get_queryset().filter(publications__isnull=False).distinct()


class PressReleaseCategoryManager(models.Manager):
    def get_queryset(self):
        return super(
            PressReleaseCategoryManager,
            self
        ).get_queryset().filter(press_releases__isnull=False).distinct()


class Category(models.Model):
    name = models.CharField(max_length=50, blank=False)
    slug = models.SlugField(max_length=50, blank=False, default='')
    description = models.CharField(max_length=255, blank=True, default='')

    objects = models.Manager()
    work_categories = WorksCategoryManager()
    publication_categories = PublicationCategoryManager()
    press_categories = PressReleaseCategoryManager()

    class Meta:
        verbose_name_plural = 'categories'
        ordering = ('name',)

    def __str__(self):
        return self.name


class Item(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, blank=False, default='')
    description = models.CharField(max_length=255, blank=True, default='')
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


class PressRelease(Item):
    category = models.ForeignKey(
        Category,
        related_name="press_releases",
        on_delete=models.CASCADE
    )
    url = models.URLField(blank=True)

    class Meta(Item.Meta):
        verbose_name = 'press release'
        verbose_name_plural = 'press releases'


class Work(Item):
    """
    team: Leave as Text in case of collaborations with external companies
    Change to ManyToManyField after consulting with owner
    """
    PLANNED = 0
    UNDER_CONSTRUCTION = 1
    COMPLETED = 2
    STATUS_CHOICES = (
        (PLANNED, 'Planned'),
        (UNDER_CONSTRUCTION, 'Under Construction'),
        (COMPLETED, 'Completed'),
    )
    category = models.ForeignKey(
        Category,
        related_name="works",
        on_delete=models.CASCADE
    )
    program = models.CharField(max_length=75, blank=True)
    status = models.IntegerField(choices=STATUS_CHOICES, blank=True, default=0)
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


class Publication(Item):
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
    medium = models.IntegerField(choices=MEDIUM_CHOICES, blank=True, default=ARTICLE)
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
