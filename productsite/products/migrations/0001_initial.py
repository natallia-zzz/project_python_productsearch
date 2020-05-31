# Generated by Django 3.0.5 on 2020-05-31 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('pr_id', models.CharField(max_length=12, primary_key=True, serialize=False, verbose_name='id')),
                ('pr_title', models.CharField(max_length=100, verbose_name='title')),
                ('pr_description', models.CharField(max_length=15000, verbose_name='description')),
                ('pr_manufacturer', models.CharField(max_length=30, verbose_name='manufacturer')),
                ('pr_price', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='price')),
            ],
        ),
    ]
