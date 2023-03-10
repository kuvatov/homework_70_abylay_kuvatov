from django import forms

from webapp.models import Issue, Type, Status, Project


class IssueForm(forms.ModelForm):
    type = forms.ModelMultipleChoiceField(
        queryset=Type.objects.all(),
        label='Тип',
        widget=forms.CheckboxSelectMultiple
    )
    status = forms.ModelChoiceField(
        queryset=Status.objects.all(),
        label='Статус'
    )

    class Meta:
        model = Issue
        fields = ('summary', 'description', 'type', 'status', 'project')
        labels = {
            'summary': 'Краткое описание',
            'description': 'Полное описание',
            'type': 'Тип',
            'status': 'Статус',
            'project': 'Проект'
        }


class SearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label="Найти")


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description', 'started_at', 'ended_at']


class ProjectIssueForm(forms.ModelForm):
    type = forms.ModelMultipleChoiceField(
        queryset=Type.objects.all(),
        label='Тип',
        widget=forms.CheckboxSelectMultiple
    )
    status = forms.ModelChoiceField(
        queryset=Status.objects.all(),
        label='Статус'
    )

    class Meta:
        model = Issue
        fields = ('summary', 'description', 'type', 'status')
        labels = {
            'summary': 'Краткое описание',
            'description': 'Полное описание',
            'type': 'Тип',
            'status': 'Статус'
        }
