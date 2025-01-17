from django import forms

from blog.models import Comment, ClientInfo, Blog
from django.contrib.auth.forms import UserCreationForm


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'message', ]
        widgets = {
            'author': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your name'}),
            'message': forms.Textarea(
                attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Enter your comment here',
                       "style": "height: 119px;"}),
        }


class ClientInfoForm(forms.ModelForm):
    class Meta:
        model = ClientInfo
        fields = ['user', 'email', 'phone_number', 'message']
        widgets = {
            'user': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),
            'phone_number': forms.TextInput(attrs={'class': "form-control", 'placeholder': 'Enter phone number'}),
            'message': forms.Textarea(
                attrs={'class': 'form-control', "rows": 10, 'placeholder': 'Enter your comment here',
                       "style": "height: 119px;"}),
        }


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("email",)


class CreatePost(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'description', 'photo']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'description': forms.Textarea(
                attrs={'class': 'form-control', 'rows': 10, 'placeholder': 'Description', 'style': 'height: 119px;'}
            ),
            'photo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }