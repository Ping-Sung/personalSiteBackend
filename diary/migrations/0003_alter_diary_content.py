# Generated by Django 4.2.1 on 2023-08-25 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0002_alter_diary_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diary',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
    ]
