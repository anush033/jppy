from django.shortcuts import render

# Create your views here.
def CourseDetailsView(r):
    return render(r,'Courses/courseDetails.html')