# Generated by Django 4.2.2 on 2023-07-26 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(max_length=255, verbose_name='Author name')),
                ('author_description', models.TextField(blank=True, null=True, verbose_name='Author information')),
            ],
        ),
    ]
