# Generated by Django 3.0.2 on 2020-04-18 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0008_auto_20200418_1533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(default='title', max_length=250),
        ),
    ]
