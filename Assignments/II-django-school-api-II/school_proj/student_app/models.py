from django.db import models
from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator


# Create your models here.
class Student(models.Model):
    name = models.CharField(
        max_length=255, 
        null = False, 
        blank = False,
        validators=[RegexValidator(r'^[A-Za-z]+ [A-Za-z]\. [A-Za-z]+$','Name must be in the format "First Middle Initial. Last"')]
    )
    student_email = models.EmailField(
        unique= True, 
        null = False, 
        blank = False,
        validators=[
            RegexValidator(r'[\w]+@school.com', 'Invalid school email format. Please use an email ending with "@school.com".')]
    )
    personal_email = models.EmailField(unique= True, null = False, blank = False)
    locker_number = models.IntegerField(
        unique= True, 
        default=110, 
        null = False, 
        blank = False,
        validators=[
            MinValueValidator(1, message="Ensure this value is greater than or equal to 1."),
            MaxValueValidator(200, message="Ensure this value is less than or equal to 200.")
            ]
        )
    locker_combination = models.CharField(
        # max_length=8,
        validators=[RegexValidator(r'^\d{2}-\d{2}-\d{2}$', 'Combination must be in the format "12-12-12"')],
        null=False,
        blank=False,
        default="12-12-12"
    )
    good_student = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} - {self.student_email} - {self.locker_number}"
    
    def locker_reassignment(self, new_locker_number):
        self.locker_number = new_locker_number
        self.save()

    def student_status(self):
        self.good_student = not self.good_student
        self.save()