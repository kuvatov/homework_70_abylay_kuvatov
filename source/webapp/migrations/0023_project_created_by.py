# Generated by Django 4.1.7 on 2023-03-21 08:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("webapp", "0022_alter_project_users"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="created_by",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="created_projects",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
