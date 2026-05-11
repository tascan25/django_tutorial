from django import forms
from .models import Tag, CommentModel

class BlogEntryForm(forms.Form):
    title = forms.CharField(max_length=200,label="Title")
    excerpt = forms.CharField(max_length=200,label="Excerpt")
    image = forms.FileField(label="Image")
    content = forms.CharField(widget=forms.Textarea, max_length=200,label="Content")
    author_first_name = forms.CharField(max_length=120, label="Author First Name")
    author_last_name = forms.CharField(max_length=120, label="Author Last Name")
    author_email = forms.EmailField(label="Author Email")
    tag = forms.ModelMultipleChoiceField(queryset=Tag.objects.all())


class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentModel
        fields = ["user_name","user_email","text"]
        labels = {
            "user_name":"Name",
            "user_email":"Email",
            "text":"Comment"
        }