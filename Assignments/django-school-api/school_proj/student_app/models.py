from django.db import models

class Student(models.Model):
    name = models.CharField(null = False, blank= False)
    student_email = models.EmailField(null = False, blank= False)
    personal_email = models.EmailField()
    locker_number = models.IntegerField(null = False, blank= False)
    locker_combination = models.CharField(null = False, blank= False)
    good_student=models.BooleanField(null = False, blank= False)