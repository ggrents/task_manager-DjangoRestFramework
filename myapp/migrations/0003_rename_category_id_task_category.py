# Generated by Django 4.2.5 on 2023-09-18 04:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_category_options_alter_task_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='category_id',
            new_name='category',
        ),
    ]