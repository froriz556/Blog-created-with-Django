from django.forms import ModelForm
from django import forms
from .models import Post

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'categories', 'text_content', 'image', 'is_published']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'categories': forms.SelectMultiple(attrs={'class': 'form-select'}),
            "text_content": forms.Textarea(attrs={'class': 'form-text','rows': 20, }),
            'image': forms.FileInput(attrs={'class': 'form-file'}),
            'is_published': forms.CheckboxInput(attrs={'class': 'form-check'}),
        }

        labels = {
            'title': "Заголовок",
            "categories": "Категории",
            "text_content": "Содержание статьи",
            "image": "Изображение",
            "is_published": "Опубликовать сразу",
        }