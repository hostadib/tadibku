from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.urls import reverse


class Tag(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Categories(models.Model):
    name = models.CharField(max_length=200)



class ArtikelPost(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, null=True, blank=True)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, null=True)
    img_artikel = models.ImageField(upload_to='Cover_blog/', blank=True)
    title = models.CharField(max_length=200, null=True, blank=True)
    writer = models.CharField(max_length=200, null=True, blank=True)
    writer_img = models.ImageField(upload_to='Writer_blog/', blank=True)
    slug = models.SlugField(max_length=200, unique=True)
    content = RichTextField(blank=True, null=True)

    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('artikel:artikel_detail', kwargs={'slug': self.slug})


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(ArtikelPost, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = RichTextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

