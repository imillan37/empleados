# Generated by Django 3.0.1 on 2020-01-10 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0004_auto_20200105_0132'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='full_name',
            field=models.CharField(blank=True, max_length=120, verbose_name='Nombres completos'),
        ),
    ]
