from django.utils.html import strip_tags
from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title", "author"]

    def clean_title(self):
        title = self.cleaned_data.get("title")

        # Remove any HTML tags
        cleaned_title = strip_tags(title)

        if title != cleaned_title:
            raise forms.ValidationError("Invalid characters detected in the title.")
        
        return cleaned_title