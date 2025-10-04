from django.db import models
from django.contrib.auth.models import User


class TypeCourse(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name="Nomi")
    descriptions = models.TextField(verbose_name="tavsifi")

    def __str__(self):
        return self.name
    

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='teacher_profiles/', blank=True, null=True)

    def __str__(self):
        return self.user.username
    

class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='courses')
    course_type = models.ForeignKey(TypeCourse, on_delete=models.SET_NULL, null=True, related_name='courses')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    

class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lessons')
    title = models.CharField(max_length=255)
    content = models.TextField()
    order = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.course.title} - {self.title}"


class LessonVideo(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='videos')
    video_url = models.URLField()
    duration = models.PositiveIntegerField(help_text="Duration in seconds")

    def __str__(self):
        return f"Video for {self.lesson.title}"


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.lesson.title}"
    

class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.PositiveIntegerField(default=1)  
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user',) 

    def __str__(self):
        return f"{self.user.username} - {self.score}"
