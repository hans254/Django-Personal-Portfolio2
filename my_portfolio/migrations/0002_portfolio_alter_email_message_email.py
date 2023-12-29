# Generated by Django 4.2.2 on 2023-09-01 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_portfolio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('title', models.CharField(max_length=10, verbose_name='Name')),
                ('description', models.CharField(max_length=50, verbose_name='Name')),
            ],
        ),
        migrations.AlterField(
            model_name='email_message',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]