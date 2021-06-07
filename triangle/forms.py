from django import forms


class TriangleForm(forms.Form):
    first_leg = forms.FloatField(label='First leg', required=True, min_value=1,
                                 help_text="Enter the length of the first leg")
    second_leg = forms.FloatField(label='Second leg', required=True, min_value=1,
                                  help_text="Enter the length of the second leg")
