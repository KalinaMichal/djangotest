# Generated by Django 3.0.5 on 2020-05-09 08:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Pydate', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('chatID', models.IntegerField(primary_key=True, serialize=False)),
                ('agreement', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='UserChat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chatID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Chat.Chat')),
                ('userID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Pydate.UserData')),
            ],
        ),
        migrations.CreateModel(
            name='ChatMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=300)),
                ('date', models.DateField(auto_now=True)),
                ('chatID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Chat.Chat')),
            ],
        ),
    ]