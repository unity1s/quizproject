# Generated by Django 3.0.8 on 2020-09-15 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('triviaapp', '0003_auto_20200915_1221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trivia',
            name='answer',
            field=models.ManyToManyField(blank=True, related_name='trivia_answer', to='triviaapp.Option'),
        ),
    ]