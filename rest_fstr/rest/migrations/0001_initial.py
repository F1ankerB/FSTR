# Generated by Django 4.2.3 on 2023-12-19 06:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coords',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('height', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='PerevalAdded',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('beautyTitle', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('other_titles', models.TextField()),
                ('connect', models.TextField()),
                ('add_time', models.DateTimeField()),
                ('status', models.CharField(default='new', max_length=50)),
                ('coord', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rest.coords')),
            ],
        ),
        migrations.CreateModel(
            name='SprActivitiesTypes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='PerevalImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.BinaryField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('pereval', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rest.perevaladded')),
            ],
        ),
        migrations.CreateModel(
            name='PerevalAreas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('id_parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rest.perevalareas')),
            ],
        ),
        migrations.AddField(
            model_name='perevaladded',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rest.user'),
        ),
    ]