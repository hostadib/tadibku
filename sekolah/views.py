from django.shortcuts import render, get_object_or_404
from .models import Sma
from django.http import Http404


def guru_list(request):
    posts = Sma.objects.all ( ).order_by ( 'date_posted' )
    context = {
        'posts' : posts,
    }
    return render ( request, 'sekolah/sma.html', context )