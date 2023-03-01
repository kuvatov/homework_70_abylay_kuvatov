from django.db import models


class IssueType(models.Model):
    name = models.CharField(
        max_length=30,
        null=False,
        blank=False,
        verbose_name="Тип"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата и время создания"
    )
    edited_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата и время редактирования"
    )

    def __str__(self):
        return self.name
