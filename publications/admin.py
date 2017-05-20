from django.contrib import admin
from django.urls import reverse

from .models import Press, Publication, Work, WorkCover, WorkPicture
from .support_models import Category, Medium, Program, Status


class WorkPictureInline(admin.StackedInline):
    model = WorkPicture
    extra = 1
    prepopulated_fields = {'slug': ('title',)}
    
class WorkCoverInline(admin.StackedInline):
    model = WorkCover
    extra = 1
    prepopulated_fields = {'slug': ('title',)}

class WorkAdmin(admin.ModelAdmin):
    fields = (
        'title',
        'slug',
        'description',
        'category',
        'program',
        'status',
        'team',
        'document',
        'published_date',
        'display_order'
    )
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'category', 'program', 'status',)
    list_filter = ('created_date', 'category', 'program', 'status',)
    list_display = ('title', 'display_order', 'category', 'program', 'status', 'published_date', '_is_published',)
    list_editable = ('category', 'status', 'program', 'published_date', 'display_order',)
    inlines = [WorkCoverInline, WorkPictureInline]


class WorkPictureAdmin(admin.ModelAdmin):
    fields = (
        'title',
        'slug',
        'image',
        'caption',
        'work',
    )
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('work', 'title',)
    list_filter = ('work',)
    list_display = ('title', 'work',)
    list_editable = ('work',)


class WorkCoverAdmin(admin.ModelAdmin):
    fields = (
        'title',
        'slug',
        'image',
        'caption',
        'work',
    )
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('work', 'title',)
    list_filter = ('work',)
    list_display = ('title', 'work',)
    list_editable = ('work', )


class PublicationAdmin(admin.ModelAdmin):
    fields = (
        'title',
        'slug',
        'description',
        'image',
        'category',
        'medium',
        'url',
        'published_date',
        'display_order',
    )
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'category',)
    list_filter = ('created_date', 'category',)
    list_display = ('title', 'display_order','category', 'medium', 'published_date', '_is_published',)
    list_editable = ('category','medium', 'published_date', 'display_order', )


class PressAdmin(admin.ModelAdmin):
    fields = (
        'title',
        'slug',
        'description',
        'url',
        'category',
        'published_date',
        'display_order'
    )
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'category',)
    list_filter = ('created_date', 'category',)
    list_display = ('title', 'display_order', 'category', 'published_date', '_is_published',)
    list_editable = ('category', 'published_date', 'display_order')

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)
    
class MediumAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)

class StatusAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)

class ProgramAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)



admin.site.register(Work, WorkAdmin)
admin.site.register(Press, PressAdmin)
admin.site.register(Publication, PublicationAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(WorkCover, WorkCoverAdmin)
admin.site.register(WorkPicture, WorkPictureAdmin)
admin.site.register(Program, ProgramAdmin)
admin.site.register(Status, StatusAdmin)
admin.site.register(Medium, MediumAdmin)


admin.site.site_header = "Estudio Caribe Administration"