from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone


def validate_summary_exists(value):
    if Issue.objects.filter(summary=value).exists():
        raise ValidationError('Краткое описание с таким названием уже существует!')


def validate_summary_min_length(value):
    if len(value) < 5:
        raise ValidationError('Краткое описание должно быть длиннее 5 символов!')


class Issue(models.Model):
    summary = models.CharField(
        max_length=50,
        null=False,
        blank=False,
        verbose_name="Краткое описание",
        validators=[
            validate_summary_exists,
            validate_summary_min_length
        ]
    )
    description = models.TextField(
        max_length=2000,
        null=True,
        blank=True,
        verbose_name="Полное описание"
    )
    status = models.ForeignKey(
        to="webapp.Status",
        on_delete=models.RESTRICT,
        null=False,
        blank=False,
        related_name="issue_statuses",
        verbose_name="Статус"
    )
    type = models.ManyToManyField(
        to="webapp.Type",
        related_name="issue_set",
        blank=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата и время создания"
    )
    edited_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата и время редактирования"
    )
    is_deleted = models.BooleanField(
        verbose_name="Deleted",
        null=False,
        default=False
    )
    deleted_date = models.DateTimeField(
        verbose_name="Date of deletion",
        null=True,
        default=None
    )

    def __str__(self):
        return f"{self.summary} | {self.status} | {self.type}"

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.deleted_date = timezone.now()
        self.save()
