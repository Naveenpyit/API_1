from django.db import models

class clgstudent(models.Model):
    student_id=models.IntegerField(primary_key=True)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    date_of_birth=models.CharField(max_length=32)
    email=models.CharField(max_length=150)
    phone=models.CharField(max_length=10)
    enrollment_date=models.CharField(max_length=20)

    class Meta:
        db_table='clgstudents'


class clgcourses(models.Model):
    course_id=models.IntegerField(primary_key=True)
    course_name=models.CharField(max_length=100)
    course_code=models.CharField(max_length=10)
    course_rank=models.IntegerField()

    class Meta:
        db_table='courses'
