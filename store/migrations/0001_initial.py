# Generated by Django 5.0.2 on 2024-02-07 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField(blank=True, max_length=200, null=True)),
                ('price', models.IntegerField(default=0)),
                ('image', models.ImageField(blank=True, null=True, upload_to='Product/')),
                ('category', models.CharField(choices=[('E', 'Electronics'), ('C', 'Clothing'), ('B', 'Books'), ('O', 'Others')], max_length=50)),
            ],
        ),
    ]
