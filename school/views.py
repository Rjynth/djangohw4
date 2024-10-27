from django.views.generic import ListView
from django.shortcuts import render
import os


from .models import Student


def student_list(request):
    students = Student.objects.prefetch_related('teachers').all()
    return render(request, 'school/student_list.html', {'students': students})

class students_list(ListView):
    template = 'school/students_list.html'

    model = Student
    ordering = 'group'
    queryset = Student.objects.all().prefetch_related('teachers')
