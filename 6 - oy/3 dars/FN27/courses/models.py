from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=200)
    descriptions = models.TextField()
    createed_at = models.TimeField(auto_now_add = True)
    updated_at = models.TimeField(auto_now = True)

    def __str__(self):
        return self.title
    
class Student(models.Model):
    name = models.CharField(max_length = 100)
    email = models.CharField(max_length = 100)
    enrolled_at = models.DateTimeField(auto_now_add = True)
    coure = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="students")

    def __str__(self):
        return self.name
    
