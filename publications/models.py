from django.db import models
from django.utils import timezone
from django.utils.text import slugify

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


class SupportModel(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, blank=True, default='')
    description = models.TextField(max_length=500, blank=True, default='')

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.full_clean()
        super(SupportModel, self).save(*args, **kwargs)

    def clean(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(SupportModel, self).clean(*args, **kwargs)

    def __str__(self):
        return self.name

class Medium(SupportModel):
    class Meta(SupportModel.Meta):
        verbose_name = 'medium'
        verbose_name_plural = 'mediums'


class Status(SupportModel):
    class Meta(SupportModel.Meta):
        verbose_name = 'status'
        verbose_name_plural = 'statuses'
        

class Program(SupportModel):
    category = models.ForeignKey(
        'Category',
        related_name="programs",
        on_delete=models.CASCADE,
        blank=True
    )
    class Meta(SupportModel.Meta):
        verbose_name = 'program'
        verbose_name_plural = 'programs'


class Category(SupportModel):
    class Meta(SupportModel.Meta):
        verbose_name_plural = 'categories'
        ordering = ('name',)


class Item(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, blank=True, default='')
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
    
    def save(self, *args, **kwargs):
        self.full_clean()
        super(Item, self).save(*args, **kwargs)

    def clean(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Item, self).clean(*args, **kwargs)

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

    def get_cover(self):
        cover = [i for i in self.pictures.all() if i.is_cover]
        if not cover:
            return None
        else:
            return cover[0]

    def set_cover(self, picture_id):
        for picture in self.pictures.all():
            if picture.id != picture_id:
                picture.is_cover = False
            else:
                picture.is_cover = True

    def clean(self, *args, **kwargs):
        self.slug = slugify(self.title)
        if self.get_cover() is not None:
            if len(self.get_cover()) > 1:
                raise ValidationError(_("One Work can't have two cover images"))
        super(Work, self).clean(*args, **kwargs)

    class Meta(Item.Meta):
        verbose_name = 'work'
        verbose_name_plural = 'works'
        ordering = ('-created_date',)
        

class WorkPicture(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, blank=False, default='')
    image = models.ImageField(upload_to=work_directory_path, blank=True, null=True)
    caption = models.TextField(blank=True)
    is_cover = models.BooleanField(default=False, blank=False)
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

    def clean(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(WorkPicture, self).clean(*args, **kwargs)

    def save(self, *args, **kwargs):
        self.full_clean()
        super(WorkPicture, self).save(*args, **kwargs)


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


