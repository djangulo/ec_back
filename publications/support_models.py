from django.db import models


class WorkItemsManager(models.Manager):
    def get_queryset(self):
        return super(
            WorkItemsManager,
            self
        ).get_queryset().filter(works__isnull=False).distinct()

         
class PublicationItemsManager(models.Manager):
    def get_queryset(self):
        return super(
            PublicationItemsManager,
            self
        ).get_queryset().filter(publications__isnull=False).distinct()


class PressReleaseItemsManager(models.Manager):
    def get_queryset(self):
        return super(
            PressReleaseItemsManager,
            self
        ).get_queryset().filter(press_releases__isnull=False).distinct()


class SupportModel(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    description = models.TextField(max_length=500, blank=True, default='')

    objects = models.Manager()
    work_items = WorkItemsManager()
    publication_items = PublicationItemsManager()
    press_items = PressReleaseItemsManager()

    class Meta:
        abstract = True
        
    def __str__(self):
        return self.name

    def all_works_list(self):
        return sorted([(w.id, w.title) for w in self.works.all()])
        
    def all_publications_list(self):
        return sorted([(p.id, p.title) for p in self.publications.all()])

    def all_press_releases_list(self):
        return sorted([(p.id, p.title) for p in self.press_releases.all()])


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