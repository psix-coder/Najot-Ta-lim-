from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Course, Lesson, Comment
from .forms import LessonForm, RegisterForm, CommentForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required 




def course_list(request):
    courses = Course.objects.all()
    return render(request, 'app/course_list.html', {'courses': courses})



def lesson_list(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    lessons = course.lessons.all()
    return render(request, 'app/lesson_list.html', {'course': course, 'lessons': lessons})



def lesson_detail(request, lesson_id):
    lesson = get_object_or_404(Lesson, pk=lesson_id)
    return render(request, 'app/lesson_detail.html', {'lesson': lesson})



def add_post(request, ):
    if request.method == 'POST':
        form = LessonForm(data=request.POST)
        if form.is_valid():
            lesson = Lesson.objects.create(
                **form.cleaned_data
            )
            return redirect('lesson_detail', lesson_id=lesson.id)

    form = LessonForm()
    context = {
        "form": form
    }
    return render(request, 'app/add_post.html', context)



def update_post(request, lesson_id):
    lesson = get_object_or_404(Lesson, id=lesson_id)
    if request.method == 'POST':
        form = LessonForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            lesson.title = form.cleaned_data.get('title')
            lesson.content = form.cleaned_data.get('content')
            lesson.course = form.cleaned_data.get('course')
            lesson.save()
 
    form = LessonForm(initial={
        'title':lesson.title,
        'content':lesson.content,
        'course':lesson.course
    })

    context = {
        "form":form 
    }
    return render(request, 'app/add_post.html', context)



def register(request, lesson_id):
    lesson = get_object_or_404(Lesson, id=lesson_id)
    form = RegisterForm()
    context = {
        "form": form,
        "lesson":lesson,
    }
    return render(request, 'auth/register.html', context)



def login_view(request):
    if request.method == 'POST':
        
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('course_list')  
        else:
            messages.error(request, 'Username yoki parol xato!')
            return redirect('login')  
    return render(request, 'auth/login.html')



def logout_view(request):
    logout(request)
    return redirect('login')


def post_detail(request, lesson_id):
    lesson = get_object_or_404(Lesson, id=lesson_id, published=True)
    lesson.views += 1
    lesson.save()

    context = {
        "lesson":lesson,
        "title":lesson.title,
        "form":CommentForm()
    }
    return render(request, )

@login_required(login_url='login/')
def create_cmment(request, lesson_id):
    if request.method == 'POST':
        author = request.user
        text = request.POST.get('text')

        lesson_id = Lesson.objects.get(id=lesson_id)
        Comment.objects.create(lesson=lesson_id, content=text, author=author)
        return redirect('lesson', lesson_id=lesson_id)
    return render(request, 'comment_edit.html') 
