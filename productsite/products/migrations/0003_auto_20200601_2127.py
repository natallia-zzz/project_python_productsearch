# Generated by Django 3.0.5 on 2020-06-01 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_basket'),
    ]

    operations = [
        migrations.RenameField(
            model_name='basket',
            old_name='prod_id',
            new_name='prod',
        ),
        migrations.RenameField(
            model_name='basket',
            old_name='user_id',
            new_name='user',
        ),
        migrations.AddField(
            model_name='basket',
            name='num',
            field=models.IntegerField(default=1),
        ),
    ]
