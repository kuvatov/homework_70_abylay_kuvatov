from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import BaseValidator, MinLengthValidator

from webapp.models import Issue, Type, Status


class CustomLenValidator(BaseValidator):
    def __init__(self, limit_value=30):
        message = 'Максимальная длина краткого описания %(limit_value)s. Вы ввели %(show_value)s символов'
        super().__init__(limit_value=limit_value, message=message)

    def compare(self, limit_value, value):
        return limit_value > value

    def clean(self, value):
        return len(value)


class IssueForm(forms.ModelForm):
    summary = forms.CharField(
        validators=(
            MinLengthValidator(
                limit_value=5,
                message='Краткое описание должно состоять минимум из 5 символов!'
            ),
            CustomLenValidator()),
        label='Краткое описание'
    )
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
