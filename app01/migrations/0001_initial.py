# Generated by Django 2.1.3 on 2019-03-06 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='课程名')),
                ('describe', models.CharField(max_length=100, verbose_name='课程描述：')),
                ('times', models.IntegerField(blank=True, null=True, verbose_name='课时')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
                ('sex', models.CharField(max_length=8)),
                ('id_card', models.CharField(max_length=30)),
                ('tel', models.CharField(max_length=30)),
                ('addr', models.CharField(max_length=100)),
                ('cs', models.ManyToManyField(to='app01.Course')),
            ],
        ),
    ]
