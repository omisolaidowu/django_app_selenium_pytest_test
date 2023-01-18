from django import forms
from .models import art_gallery
from .models import *

from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget


class my_engine(forms.ModelForm):
	published = forms.BooleanField(required=False).widget.attrs.update({'id': 'published'})
	title = forms.CharField(widget=forms.Textarea(attrs={
		"rows":1, 
		"cols":70, 
		"placeholder":"Enter the Title of your work",
		"class":"my-title"
		}))
	content = forms.CharField(widget=forms.Textarea(attrs={
		"class": "content-field"
		}))
	desc_of_art = forms.CharField(widget=forms.Textarea(attrs={
		"rows":10, 
		"cols":70, 
		"placeholder":"Enter a short description of your art work",
		"class":"-content-description"
		}))
	pictures  = forms.ImageField(label='upload an image').widget.attrs.update({'class': 'image-upload'})
	
	class Meta:
		model = art_gallery
		fields=('published','title', 'content', 'desc_of_art')


