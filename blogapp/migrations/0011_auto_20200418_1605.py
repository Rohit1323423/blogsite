# Generated by Django 3.0.2 on 2020-04-18 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0010_auto_20200418_1551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='status',
            field=models.CharField(choices=[('Default', 'Draft'), ('Publish', 'Publish')], default='Default', max_length=20),
        ),
    ]
