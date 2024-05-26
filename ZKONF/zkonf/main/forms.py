from django import forms
from .models import Participant, ScientificWork


class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ['first_name', 'last_name', 'works']

    def clean(self):
        cleaned_data = super().clean()
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')
        if Participant.objects.filter(first_name=first_name, last_name=last_name).exists():
            raise forms.ValidationError("A participant with this first name and last name already exists.")
        return cleaned_data
    

class ScientificWorkForm(forms.ModelForm):
    class Meta:
        model = ScientificWork
        fields = ['title', 'authors', 'year_of_publication', 'areas']

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if ScientificWork.objects.filter(title=title).exists():
            raise forms.ValidationError("A ScientificWork with this title already exists.")
        return title