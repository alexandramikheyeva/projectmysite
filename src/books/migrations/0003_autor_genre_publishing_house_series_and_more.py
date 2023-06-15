# Generated by Django 4.2.2 on 2023-06-15 16:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_alter_book_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('autor_name', models.CharField(max_length=50)),
                ('autor_description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre_name', models.CharField(max_length=50)),
                ('genre_description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Publishing_House',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publishing_house_name', models.CharField(max_length=50)),
                ('publishing_house_description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('series_name', models.CharField(max_length=100)),
                ('series_description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='book',
            name='description',
        ),
        migrations.AddField(
            model_name='book',
            name='ISBN',
            field=models.CharField(default=1, max_length=25),
        ),
        migrations.AddField(
            model_name='book',
            name='active',
            field=models.CharField(choices=[('Y', 'active'), ('N', 'inactive')], default=1, max_length=4),
        ),
        migrations.AddField(
            model_name='book',
            name='age_restrictions',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=3),
        ),
        migrations.AddField(
            model_name='book',
            name='binding',
            field=models.CharField(choices=[('Solid', 'solid'), ('Soft', 'soft'), ('Absent', 'absent')], default=1, max_length=6),
        ),
        migrations.AddField(
            model_name='book',
            name='counter_book',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=7),
        ),
        migrations.AddField(
            model_name='book',
            name='format_book',
            field=models.CharField(choices=[('Super small', '84x108/64'), ('Small', '75x90/32'), ('Standart', '60x90/16'), ('Bigger', '70x108/16'), ('Big', '60x90/8'), ('Super big', '84x108/8')], default=1, max_length=12),
        ),
        migrations.AddField(
            model_name='book',
            name='image',
            field=models.ImageField(blank=True, upload_to='book/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='book',
            name='page',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=6),
        ),
        migrations.AddField(
            model_name='book',
            name='rating',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=2),
        ),
        migrations.AddField(
            model_name='book',
            name='weight',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=6),
        ),
        migrations.AddField(
            model_name='book',
            name='year_publishing',
            field=models.DateField(default=5, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='genre',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='books.genre'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='publishing_house',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.PROTECT, to='books.publishing_house'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='series',
            field=models.ForeignKey(default=4, on_delete=django.db.models.deletion.PROTECT, to='books.series'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.autor'),
        ),
    ]
