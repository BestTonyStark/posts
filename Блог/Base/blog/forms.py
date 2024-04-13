from django import forms


class AddPostForm(forms.Form):
    title = forms.CharField(max_length=64, min_length=2)
    content = forms.CharField()
    image = forms.ImageField()
    author_user_name = forms.CharField(max_length=30)
