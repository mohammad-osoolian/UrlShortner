# Generated by Django 3.2.6 on 2021-08-28 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shortner', '0004_alter_url_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='key',
            field=models.CharField(default='key', max_length=255),
            preserve_default=False,
        ),
    ]
