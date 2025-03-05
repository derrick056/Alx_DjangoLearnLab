from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title", "author"]

    def clean_title(self):
        title = self.cleaned_data.get("title")
        if "<script>" in title:
            raise forms.ValidationError("Invalid input detected")
        return title

# ExampleForm Definition (Modify as needed)
class ExampleForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

    def clean_message(self):
        message = self.cleaned_data.get("message")
        if "<script>" in message:
            raise forms.ValidationError("Invalid input detected")
        return message