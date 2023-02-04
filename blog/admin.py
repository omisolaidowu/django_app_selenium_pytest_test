from django.contrib import admin

# Register your models here.
from .models import art_gallery



# class AdminPost(SummernoteModelAdmin):
# 	summernote_fields = ('about_art', 'desc_of_art',)


# Register your models here.
admin.site.register(art_gallery)

