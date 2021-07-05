from datetime import timedelta

from django import forms
from django.utils import timezone


# HT 12. Celery
class ReminderForm(forms.Form):
    email = forms.EmailField(required=True, max_length=254, initial='test@gmail.com',
                             help_text='Enter the email for sending the reminder')
    text = forms.CharField(required=True, widget=forms.Textarea(attrs={'rows': 3}), initial="Do your homework",
                           help_text='Enter the reminder')
    time_sending = forms.DateTimeField(required=True, initial=timezone.now(), input_formats={'%Y-%m-%D %H:%M'},
                                       widget=forms.TextInput(attrs={'placeholder': 'YYYY-MM-DD HH:MM'}),
                                       help_text='Enter a date no more than 2 days from the current date')

    def clean_time_sending(self):
        time = self.cleaned_data['time_sending']
        if time < timezone.now():
            raise forms.ValidationError('Invalid date. The date must be no earlier than the current date.')
        if time > timezone.now() + timedelta(days=2):
            raise forms.ValidationError('Invalid date. The date must be no later than 2 days.')
        return time
