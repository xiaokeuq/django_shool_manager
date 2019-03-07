from django.db import models

# Create your models here.
class Student(models.Model):

    name = models.CharField(max_length=20)
    age = models.IntegerField()
    sex = models.CharField(max_length=8)
    id_card = models.CharField(max_length=30)
    tel = models.CharField(max_length=30)
    addr = models.CharField(max_length=100)
    cs = models.ManyToManyField("Course")


class Course(models.Model):
    name = models.CharField('课程名', max_length=100)
    describe = models.CharField('课程描述：', max_length=100)
    times = models.IntegerField('课时', blank=True, null=True)
