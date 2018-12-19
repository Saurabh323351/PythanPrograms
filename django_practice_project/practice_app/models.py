from django.db import models

# Create your models here.



class Employee(models.Model):
    ename = models.CharField(max_length=30)
    eid = models.IntegerField()
    e_department = models.CharField(max_length=50)
    e_post = models.CharField(max_length=50)
    e_address = models.CharField(max_length=50)

    def __str__(self):
        return self.e_post

class Student(models.Model):
    st_name=models.CharField(max_length=50)
    st_rollno=models.IntegerField()
    st_address=models.CharField(max_length=50)
    st_qualification=models.CharField(max_length=10)
