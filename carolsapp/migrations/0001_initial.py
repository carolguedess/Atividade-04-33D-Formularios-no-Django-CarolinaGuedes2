# Generated by Django 3.2.13 on 2023-09-02 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='sucessos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('peças', models.CharField(max_length=50)),
                ('evoluçao', models.CharField(max_length=50)),
                ('estampas', models.CharField(max_length=60)),
                ('gênero', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='transformacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('frequencia', models.CharField(max_length=50)),
                ('over_the_years', models.CharField(choices=[('B', 'before 70'), ('W', 'while'), ('A', 'after 2000')], max_length=1)),
                ('ordem', models.IntegerField()),
            ],
        ),
    ]
