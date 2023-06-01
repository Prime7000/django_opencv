from django.contrib import admin

# Register your models here.
from .models import Upload

class PostAdmin(admin.ModelAdmin):
    pass

admin.site.register(Upload, PostAdmin)
