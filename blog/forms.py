from django import forms
from django.core.exceptions import ValidationError
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'slug', 'content')

        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control'}),
            'slug' : forms.TextInput(attrs={'class' : 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'})
        }

    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()

        if new_slug == 'create':
            raise ValidationError('slug may not be "Create"')
        return new_slug