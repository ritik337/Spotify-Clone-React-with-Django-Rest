# Generated by Django 4.2.4 on 2023-12-15 09:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='geners',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Gener', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='playlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Play_List_Name', models.CharField(max_length=80)),
                ('Singer_Name', models.CharField(max_length=80)),
                ('Playlist_Cover', models.ImageField(upload_to='media/playlistcovers')),
                ('Gener', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='playlists.geners')),
            ],
        ),
        migrations.CreateModel(
            name='songs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Song_Name', models.CharField(max_length=80)),
                ('Song_Cover', models.ImageField(upload_to='media/song/covers')),
                ('Song_Dur', models.IntegerField()),
                ('Song_File', models.FileField(upload_to='media/songs')),
                ('Play_List_Name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='playlists.playlist')),
            ],
        ),
    ]
