# Generated by Django 4.1 on 2022-09-07 12:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('advertisements', '0005_favorite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favorite',
            name='ad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='advertisements.advertisement'),
        ),
        migrations.AlterField(
            model_name='favorite',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
