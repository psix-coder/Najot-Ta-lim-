from django import forms
from app.models import Course, Lesson
from django.contrib.auth.models import User

class LessonForm(forms.Form):
    title = forms.CharField(max_length=100, widget=forms.TextInput(), label='Nomi', required=False)
    content = forms.CharField(widget=forms.Textarea(), label='Contenti', required=False)
    course = forms.ModelChoiceField(queryset=Course.objects.all(), widget=forms.Select(), label="Kursi", required=False)


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=50, widget=forms.TextInput(), label='F.I.O', required=False)
    email = forms.EmailField(max_length=50, widget=forms.EmailInput(), label='Email', required=False)
    password = forms.CharField(min_length=8, widget=forms.PasswordInput(), label='Parol', required=False)
    password_repeat = forms.CharField(min_length=8, widget=forms.PasswordInput(), label='Parol', required=False)


class CommentForm(forms.Form):
    text = forms.CharField(max_length=300, widget=forms.Textarea(), label='Comment', required=False)
    author = forms.ModelChoiceField(queryset=User.objects.all(), widget=forms.Select(), label="Author", required=False)
    post = forms.ModelChoiceField(queryset=Lesson.objects.all(), widget=forms.Select(), label="Post", required=False)
    comment_at = forms.ModelChoiceField(queryset=Lesson.objects.all(), widget=forms.Select(), label="comment_date", required=False)
    

    
