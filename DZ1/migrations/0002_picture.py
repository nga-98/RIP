# Generated by Django 2.1.3 on 2019-01-16 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DZ1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='static/photo')),
            ],
        ),
    ]
