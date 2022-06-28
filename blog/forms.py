from django import forms

from .models import Post, Reaction

class PostForm(forms.ModelForm):
  
  class Meta:
    model = Post
    fields = ('title', 'text')
    
class ReactionForm(forms.ModelForm):
  
  class Meta:
    model = Reaction
    fields = ('author', 'title', 'text')
    