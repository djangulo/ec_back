from django.contrib import admin

# Register your models here.
from .models import Work, Publication, PressRelease, Category, WorkPicture

admin.site.register(Work)
admin.site.register(PressRelease)
admin.site.register(Publication)
admin.site.register(Category)
admin.site.register(WorkPicture)