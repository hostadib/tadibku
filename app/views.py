from django.shortcuts import render
from .models import Categories, Course

def BASE(request):
    return render(request, 'base.html')

def HOME(request):
    category = Categories.objects.all().order_by('id')[0:6]
    course = Course.objects.all().filter(status = 'PUBLISH').order_by('-id')
    context = {

        'category': category,
        'course': course,
    }

    return render(request, 'main/home.html', context)

def SIGNLE_COURSE(request):

    return render(request, 'main/course.html')

def CONTACT_US(request):
    return render(request, 'main/contact.html')
# Create your views here.
