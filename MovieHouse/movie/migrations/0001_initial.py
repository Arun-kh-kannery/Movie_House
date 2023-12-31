# Generated by Django 4.2.6 on 2023-10-26 17:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genere',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genere', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mname', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='movie/movies')),
                ('year', models.CharField(max_length=50)),
                ('duration', models.CharField(max_length=100)),
                ('rating_outof_10', models.IntegerField()),
                ('description', models.TextField()),
                ('trending', models.BooleanField(default=False)),
                ('video', models.FileField(max_length=500, upload_to='movies/videos')),
                ('status', models.CharField(max_length=100)),
                ('genere', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.genere')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.language')),
            ],
        ),
    ]
