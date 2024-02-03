from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.edit import CreateView
from bs4 import BeautifulSoup
from .models import ArtikelPost, Post, Tag, Comment, Categories
from .forms import CommentForm
from django.http import JsonResponse


def artikel_list(request):
    posts = ArtikelPost.objects.all().order_by('date_posted')[0:4]
    categories = Categories.objects.all().order_by('id')[0:7]
    artikel = ArtikelPost.objects.all()
    recent_posts = ArtikelPost.objects.all().order_by('id')[0:3]

    context = {
        'posts': posts,
        'categories' : categories,
        'recent_posts': recent_posts,
        'artikel': artikel,
    }
    return render(request, 'artikel/artikel_list.html', context)

def artikel_detail(request, slug):
    post = get_object_or_404(ArtikelPost, slug=slug)
    comments = post.comments.order_by('-created_date')  # get comments for this post
    latest_posts = ArtikelPost.objects.order_by('-date_posted')[:3]  # Get the latest 3 posts
    tags = Tag.objects.all()

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user  # set the user to the logged in user
            comment.save()
            return redirect('artikel:artikel_detail', slug=post.slug)
    else:
        form = CommentForm()

    context = {
        'post': post,
        'comments': comments,
        'form': form,
        'latest_posts': latest_posts,
        'tags': tags
    }

    return render(request, 'artikel/artikel_detail.html', context)



class ArtikelPostCreateView(CreateView):
    model = ArtikelPost
    fields = ['title', 'content', 'writer', 'writer_img', 'cite']

    def form_valid(self, form):
        content = form.cleaned_data.get('content')
        soup = BeautifulSoup(content, 'html.parser')
        text_only_content = soup.get_text()
        form.instance.content = text_only_content

        return super().form_valid(form)


def filter_data ( request ) :
    if request.method == 'GET' :
        categories = request.GET.getlist ( 'category[]' )
        filtered_articles = ArtikelPost.objects.filter ( tag__in=categories )

        response_data = {
            'success' : True,
            'filtered_articles' : list ( filtered_articles.values ( ) ),  # Ubah sesuai dengan kebutuhan Anda
        }
        return JsonResponse ( response_data, safe=False )

    response_data = {'success' : False, 'message' : 'Invalid request method'}
    return JsonResponse ( response_data )