from django.db import models


class Issue(models.Model):
    summary = models.CharField(
        max_length=50,
        null=False,
        blank=False,
        verbose_name="Краткое описание"
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

    def __str__(self):
        return f"{self.summary} | {self.status} | {self.type}"
