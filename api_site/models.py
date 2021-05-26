from django.db import models

# Create your models here.
class Teacher(models.Model):
    name = models.CharField(primary_key=True, max_length=90)
    email = models.CharField(max_length=90)
    password = models.CharField(max_length=90)

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(primary_key=True, max_length=90)
    email = models.CharField(max_length=90)
    password = models.CharField(max_length=90)

    def __str__(self):
        return self.name
