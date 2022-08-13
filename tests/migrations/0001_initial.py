# Generated by Django 4.0.6 on 2022-07-21 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(max_length=500)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('score', models.IntegerField(default=1)),
                ('answer', models.CharField(choices=[('True', 'True'), ('False', 'False')], max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Subjects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('attempts', models.IntegerField(default=1)),
                ('questions', models.ManyToManyField(to='tests.questions')),
            ],
        ),
        migrations.AddField(
            model_name='questions',
            name='subjects',
            field=models.ManyToManyField(to='tests.subjects'),
        ),
    ]
