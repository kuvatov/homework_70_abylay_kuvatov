from django.db import models
from django.utils import timezone


class Project(models.Model):
    started_at = models.DateField(
        null=False,
        blank=False,
        verbose_name="Дата начала",
        default=timezone.now
    )
    ended_at = models.DateField(
        null=True,
        blank=True,
        verbose_name="Дата окончания"
    )
    name = models.CharField(
        max_length=50,
        null=False,
        blank=False,
        verbose_name="Название"
    )
    description = models.TextField(
        max_length=2000,
        null=True,
        blank=True,
        verbose_name="Описание"
    )
    is_deleted = models.BooleanField(
        verbose_name="Удален",
        null=False,
        default=False
    )
    deleted_date = models.DateTimeField(
        verbose_name="Дата и время удаления",
        null=True,
        default=None
    )

    def __str__(self):
        return self.name

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.deleted_date = timezone.now()
        self.save()
