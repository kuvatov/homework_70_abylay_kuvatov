from django import forms
from django.core.exceptions import ValidationError

from webapp.models import Issue, Type, Status


class IssueForm(forms.ModelForm):
    type = forms.ModelMultipleChoiceField(queryset=Type.objects.all(), label='Тип')
    status = forms.ModelChoiceField(queryset=Status.objects.all(), label='Статус')

    class Meta:
        model = Issue
        fields = ('summary', 'description', 'type', 'status')
        labels = {
            'summary': 'Краткое описание',
            'description': 'Полное описание',
            'type': 'Тип',
            'status': 'Статус'
        }

    def clean_summary(self):
        summary = self.cleaned_data.get('summary')
        if len(summary) < 5:
            raise ValidationError('Краткое описание должно состоять минимум из 5 символов!')
        return summary.capitalize()
