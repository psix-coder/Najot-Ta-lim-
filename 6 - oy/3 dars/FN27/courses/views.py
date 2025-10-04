from django.shortcuts import render
from .models import Course

def course_list(request):
    courses = Course.objects.prefetch_related("students").all()
    return render(request, 'courses/course_list.html', {'courses':courses})


