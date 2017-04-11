from django.contrib import admin

# Register your models here.
from .models import Work, Publication, PressRelease, Category, WorkPicture

class WorkAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

class PublicationAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

class PressReleaseAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Work, WorkAdmin)
admin.site.register(PressRelease, PressReleaseAdmin)
admin.site.register(Publication, PublicationAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(WorkPicture)