from django import forms

from webapp.models import Poll,Choice


class PollForm(forms.ModelForm):
    class Meta:
        model = Poll
        exclude = ['created_at', 'updated_at']

class ChoiceForm(forms.ModelForm):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


    class Meta:
        model = Choice
        fields = ['text', 'poll']


class PollChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ['text']