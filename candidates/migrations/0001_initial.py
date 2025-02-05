# Generated by Django 3.0.7 on 2020-06-14 02:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CandidateProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pimage', models.ImageField(default='default.jpg', upload_to='cand_pics')),
                ('fir_name', models.CharField(max_length=100)),
                ('las_name', models.CharField(max_length=100)),
                ('run_party', models.CharField(max_length=240)),
                ('cand_plat', models.TextField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
