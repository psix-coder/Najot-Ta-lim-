from django.shortcuts import render, get_object_or_404
from .models import Course, Lesson


def course_list(request):
    courses = Course.objects.all()
    return render(request, 'by_tur.html', {'courses': courses})


def lesson_list(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    lessons = course.lessons.all()
    return render(request, 'by_detail.html', {'course': course, 'lessons': lessons})


def lesson_detail(request, lesson_id):
    lesson = get_object_or_404(Lesson, pk=lesson_id)
    return render(request, 'type.html', {'lesson': lesson})
