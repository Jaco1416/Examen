# Generated by Django 3.1.2 on 2023-07-12 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20230707_2129'),
    ]

    operations = [
        migrations.AddField(
            model_name='detallescompra',
            name='usuario',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]