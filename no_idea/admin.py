from django.contrib import admin

# Register your models here.
from .models import art_gallery
# from .models import category
from django_summernote.admin import SummernoteModelAdmin


class AdminPost(SummernoteModelAdmin):
	summernote_fields = ('about_art', 'desc_of_art',)


# Register your models here.
admin.site.register(art_gallery, AdminPost)
# admin.site.register(category)

