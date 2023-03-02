from django import forms
from django.core.exceptions import ValidationError

from webapp.models import Issue, IssueType, IssueStatus


class IssueForm(forms.ModelForm):
    type = forms.ModelChoiceField(queryset=IssueType.objects.all())
    status = forms.ModelChoiceField(queryset=IssueStatus.objects.all())

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
