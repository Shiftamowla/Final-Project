from django.db import models
from django.contrib.auth.models import AbstractUser

class Custom_user(AbstractUser):
    USER=[
        ('student','Student'),
        ('teacher','Teacher'),
        ('authority','Authority')
    ]
    Gender=[
        ('male','Male'),
        ('female','Female'),
        ('other','Other')
    ]
    user_type=models.CharField(choices=USER,max_length=100,null=True)
    gender=models.CharField(choices=Gender,max_length=100,null=True)
    profile_picture=models.ImageField(upload_to='company_logos/', null=True)

    def  __str__(self):
        return f"{self.username}-{self.first_name}-{self.last_name}-{self.user_type}"
    

class Studentmodel(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    email = models.EmailField()
    phone = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Teachermodel(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    email = models.EmailField()
    phone = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


    
    
class Coursemodel(models.Model):
    course_name = models.CharField(max_length=100)
    credits = models.IntegerField()
    instructor = models.ForeignKey(Custom_user, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.course_name


class Attendancemodel(models.Model):
    student = models.ForeignKey(Studentmodel, on_delete=models.CASCADE)
    course = models.ForeignKey(Coursemodel, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=10, choices=[('Present', 'Present'), ('Absent', 'Absent'), ('Late', 'Late')])

    class Meta:
        unique_together = ('student', 'course', 'date')

    def __str__(self):
        return f"Attendance for {self.student} in {self.course} on {self.date}"



class Librarymodel(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13)
    available_copies = models.IntegerField()

    def __str__(self):
        return f"{self.title},{self.author}"
    
class AcademicCalendar(models.Model):
    year = models.CharField(max_length=10)
    term = models.CharField(max_length=20, choices=[('Fall', 'Fall'), ('Spring', 'Spring'), ('Summer', 'Summer')])
    start_date = models.DateField()
    end_date = models.DateField()
    holidays = models.TextField(blank=True)  # Can store holidays as a text list

    def __str__(self):
        return f"{self.year} {self.term} Academic Calendar"


class Result(models.Model):
    student = models.ForeignKey(Studentmodel, on_delete=models.CASCADE)
    course = models.ForeignKey(Coursemodel, on_delete=models.CASCADE)
    term = models.CharField(max_length=20)
    score = models.DecimalField(max_digits=5, decimal_places=2)
    comments = models.TextField(blank=True)

    class Meta:
        unique_together = ('student', 'course', 'term')

    def __str__(self):
        return f"{self.student} - {self.score} in {self.course} for {self.term}"


class ClassSchedule(models.Model):
    course = models.ForeignKey(Coursemodel, on_delete=models.CASCADE)
    instructor = models.ForeignKey(Studentmodel, on_delete=models.CASCADE)
    day_of_week = models.CharField(max_length=10, choices=[
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    ])
    start_time = models.TimeField()
    end_time = models.TimeField()
    classroom = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.course} - {self.instructor} on {self.day_of_week} from {self.start_time} to {self.end_time}"

