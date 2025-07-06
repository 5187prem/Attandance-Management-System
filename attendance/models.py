from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    student_id = models.CharField(max_length=10, unique=True)
    email = models.EmailField(default='')

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.student_id})"


class Course(models.Model):
    course_name = models.CharField(max_length=100)
    course_code = models.CharField(max_length=10, unique=True)
    students = models.ManyToManyField(Student, related_name='courses')

    def __str__(self):
        return self.course_name


class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.BooleanField(default=False)  # True for Present, False for Absent

    def __str__(self):
        return f"{self.student.first_name} {self.student.last_name} ({self.student.student_id}) - {self.course.course_name} on {self.date} : {'Present' if self.status else 'Absent'}"
