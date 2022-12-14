from django import forms
from . models import posts

class PostForm(forms.ModelForm):
    class Meta:
        model = posts
        fields = ('title', 'content', 'metades',)
        widgets = {
            'title':forms.TextInput(),
            'content':forms.Textarea(),
            'metades':forms.TextInput(),
        }