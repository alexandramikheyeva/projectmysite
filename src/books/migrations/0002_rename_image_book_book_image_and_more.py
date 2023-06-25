# Generated by Django 4.2.2 on 2023-06-25 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='image',
            new_name='book_image',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='title',
            new_name='book_name',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='price',
            new_name='book_price',
        ),
        migrations.AlterField(
            model_name='autor',
            name='autor_description',
            field=models.TextField(blank=True, null=True, verbose_name='Autor description'),
        ),
        migrations.AlterField(
            model_name='autor',
            name='autor_name',
            field=models.CharField(max_length=50, verbose_name='Autor name'),
        ),
        migrations.AlterField(
            model_name='genre',
            name='genre_description',
            field=models.TextField(blank=True, null=True, verbose_name='Genre description'),
        ),
        migrations.AlterField(
            model_name='genre',
            name='genre_name',
            field=models.CharField(max_length=50, verbose_name='Genre'),
        ),
        migrations.AlterField(
            model_name='publishing_house',
            name='publishing_house_description',
            field=models.TextField(blank=True, null=True, verbose_name='Publishing house description'),
        ),
        migrations.AlterField(
            model_name='publishing_house',
            name='publishing_house_name',
            field=models.CharField(max_length=50, verbose_name='Publishing house name'),
        ),
        migrations.AlterField(
            model_name='series',
            name='series_description',
            field=models.TextField(blank=True, null=True, verbose_name="Count book's series"),
        ),
        migrations.AlterField(
            model_name='series',
            name='series_name',
            field=models.CharField(max_length=100, verbose_name='Series'),
        ),
    ]