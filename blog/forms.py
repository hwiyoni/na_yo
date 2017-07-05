from django import forms
from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('how', 'when', 'so', )

class PostSearchForm(forms.Form):
	search_word = forms.CharField(label = '나는 요즘에')