# Generated by Django 4.1.7 on 2023-03-02 18:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("webapp", "0003_alter_issuestatus_options"),
    ]

    operations = [
        migrations.RenameModel(old_name="IssueStatus", new_name="Status",),
        migrations.RenameModel(old_name="IssueType", new_name="Type",),
    ]
