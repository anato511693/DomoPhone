# Generated by Django 2.1.5 on 2019-01-27 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('firstname', models.CharField(max_length=15)),
                ('lastname', models.CharField(max_length=15)),
                ('birthday', models.DateField()),
                ('email', models.EmailField(blank=True, default=None, max_length=254, null=True)),
                ('phone', models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=15)),
                ('activ', models.BooleanField(default=True)),
            ],
        ),
    ]