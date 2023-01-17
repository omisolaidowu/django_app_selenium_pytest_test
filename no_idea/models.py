from django.db import models
import os
from django.contrib.auth.models import User
from django.conf import settings
from django.utils.text import slugify
from django.urls import reverse
from django.db.models.signals import pre_save
from django.contrib.contenttypes.models import ContentType
from comments.models import Comment
from markdown_deux import markdown
from django.utils.safestring import mark_safe


def upload_location(instance, filename):
    return "%s/%s" %(instance.id, filename)


# Create your models here.
# class category(models.Model):
#     name = models.CharField(max_length=200)
#     slug = models.SlugField()

#     def __str__(self):
#         return self.name

class art_gallery(models.Model):
    user         = models.ForeignKey(
        settings.AUTH_USER_MODEL, default=id('User'), on_delete=models.CASCADE,
        blank=True, null=True
        )
    
    published = models.BooleanField(default=False)
    slug        = models.SlugField(unique=True)
    title        = models.TextField(max_length=80)
    desc_of_art    = models.TextField(max_length=100000)
    date_created   = models.DateTimeField(auto_now=True)
    content      = models.TextField(max_length=10000)
    # pictures = models.ImageField(upload_to='pictures')


    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("eachpost", kwargs={"slug": self.slug})

    def get_markdown(self):
        about_art = self.content
        markdown_text = markdown(content)
        return mark_safe(markdown_text)

    @property
    def comments(self):
        instance = self
        qs = Comment.objects.filter_by_instance(instance)

        return qs

    @property
    def get_content_type(self):
        instance = self
        content_type = ContentType.objects.get_for_model(instance.__class__)
        return content_type
    



def createslug(instance, new_slug=None):
    slug =  slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = art_gallery.objects.filter(slug=slug)
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug, qs.first().id)
        return createslug(instance, new_slug=new_slug)
    return slug

def presavesignal(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = createslug(instance)


pre_save.connect(presavesignal, sender=art_gallery)