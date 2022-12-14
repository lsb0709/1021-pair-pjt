from django import forms
from .models import Review, Comment

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['title', 'content', 'movie_name', 'grade']
        labels = {
            'title':'제목',
            'content':'내용',
            'movie_name':'영화제목',
            'grade':'평점'
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        labels = {
            'content':'댓글'
        }