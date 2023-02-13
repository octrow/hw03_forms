from django import forms

from .models import Group, Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("text", "group")

    group = forms.ModelChoiceField(
        queryset=Group.objects.all(), required=False
    )
    text = forms.CharField(widget=forms.Textarea, help_text="")
