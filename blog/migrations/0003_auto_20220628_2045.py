# Generated by Django 3.2.13 on 2022-06-28 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20220628_2044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='reaction',
            name='text',
            field=models.TextField(),
        ),
    ]
