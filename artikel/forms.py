from django import forms
from .models import Comment
from django.utils import timezone

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)


class EventForm(forms.ModelForm):
    class Meta:

        fields = ['date', 'start_time', 'end_time', 'location', 'title', 'text']

    def clean_date(self):
        date = self.cleaned_data.get('date')
        if date < timezone.now().date():
            raise forms.ValidationError("The date cannot be in the past.")
        return date