from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .models import Student, Course, Attendance
from django.utils import timezone

def add_student(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        student_id = request.POST.get('student_id')
        email = request.POST.get('email')
        Student.objects.create(first_name=first_name, last_name=last_name, student_id=student_id, email=email)
        return redirect('student_list')
    return render(request, 'attendance/add_student.html')

def add_course(request):
    if request.method == 'POST':
        course_name = request.POST.get('course_name')
        course_code = request.POST.get('course_code')
        Course.objects.create(course_name=course_name, course_code=course_code)
        return redirect('course_list')
    return render(request, 'attendance/add_course.html')

def add_attendance(request):
    if request.method == 'POST':
        student_id = request.POST.get('student_id')
        course_id = request.POST.get('course_id')
        status = request.POST.get('status') == 'Present'
        student = Student.objects.get(id=student_id)
        course = Course.objects.get(id=course_id)
        attendance = Attendance.objects.create(student=student, course=course, date=timezone.now(), status=status)
        
        # Send email notification
        subject = 'Attendance Notification'
        message = f'Hello {student.first_name},\n\nYour attendance for the course {course.course_name} has been marked as {"Present" if status else "Absent"} on {attendance.date.strftime("%Y-%m-%d")}.\n\nBest regards,\nGuru Nanak Engineering College'
        recipient_list = [student.email]
        send_mail(subject, message, 'your-email@example.com', recipient_list)

        return redirect('attendance_list')
    
    students = Student.objects.all()
    courses = Course.objects.all()
    return render(request, 'attendance/add_attendance.html', {'students': students, 'courses': courses})

def attendance_list(request):
    attendances = Attendance.objects.all().order_by('date')
    return render(request, 'attendance/attendance_list.html', {'attendances': attendances})

def student_list(request):
    students = Student.objects.all()
    return render(request, 'attendance/student_list.html', {'students': students})

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'attendance/course_list.html', {'courses': courses})
def base(request):
    return render(request,"attendance/base.html")