# Generated by Django 5.0.4 on 2024-04-06 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cakes', '0003_cake_weight'),
    ]

    operations = [
        migrations.AddField(
            model_name='cake',
            name='ingredients',
            field=models.TextField(default=0, max_length=500),
            preserve_default=False,
        ),
    ]
