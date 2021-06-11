from django import forms

from .models import Person


# Home task 6. Django: Hypotenuse calculator
class TriangleForm(forms.Form):
    first_leg = forms.FloatField(label='First leg', required=True, min_value=1,
                                 help_text="Enter the length of the first leg")
    second_leg = forms.FloatField(label='Second leg', required=True, min_value=1,
                                  help_text="Enter the length of the second leg")


# Home task 7. ModelForm for Person
class PersonModelForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'email']
