# Generated by Django 3.0.7 on 2021-02-18 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='County',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField(max_length=2, verbose_name='County Code')),
                ('name', models.CharField(max_length=100, verbose_name='County Name')),
            ],
            options={
                'verbose_name': 'County',
                'verbose_name_plural': 'Counties',
                'ordering': ('code',),
            },
        ),
        migrations.AlterModelOptions(
            name='tribe',
            options={'ordering': ('name',)},
        ),
        migrations.AlterField(
            model_name='faculty',
            name='code',
            field=models.CharField(max_length=20, verbose_name='Faculty Code'),
        ),
    ]