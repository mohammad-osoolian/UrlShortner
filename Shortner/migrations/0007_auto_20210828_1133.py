# Generated by Django 3.2.6 on 2021-08-28 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shortner', '0006_alter_url_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='key',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='url',
            name='url',
            field=models.TextField(),
        ),
    ]