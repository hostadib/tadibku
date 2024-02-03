from ckeditor.fields import RichTextField
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify
from django.db.models.signals import pre_save


# Create your models here.
class Categories(models.Model):
    icon = models.CharField(max_length=200,null=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def get_all_category(self):
        return Categories.objects.all().order_by('id')


class Author(models.Model):
    image_author = models.ImageField(upload_to="author/",null=True)
    name = models.CharField(max_length=100, null=True)
    about_author = RichTextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Level(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Course(models.Model):
    STATUS = (
        ('PUBLISH','PUBLISH'),
        ('DRAFT', 'DRAFT'),
    )
    LANGUAGE_CHOICES = (
        ('ENGLISH','ENGLISH'),
        ('INDONESIA','INDONESIA'),
        ('ARABIC','ARABIC'),
    )

    featured_image = models.ImageField(upload_to="featured_img/",null=True)
    featured_video = models.CharField(max_length=300,null=True)
    title = models.CharField(max_length=500)
    created_at = models.DateField(auto_now_add=True)
    author = models.ForeignKey(Author,on_delete=models.CASCADE,null=True)
    category = models.ForeignKey(Categories,on_delete=models.CASCADE)
    level = models.ForeignKey(Level,on_delete=models.CASCADE,null=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=0, null=True, default=0)
    discount = models.IntegerField(null=True)
    slug = models.SlugField(default='', max_length=500, null=True, blank=True)
    status = models.CharField(choices=STATUS,max_length=100,null=True)
    language = models.CharField(choices=LANGUAGE_CHOICES,max_length=100,null=True)


    def __str__(self):
        return self.title

    def formatted_price(self):
        return f"Rp {self.price:,.0f}"

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("course_detail", kwargs={"slug": self.slug})

    def discounted_price(self):
        if self.discount:
            discount_amount = self.price * self.discount / 100
            discounted_price = self.price - discount_amount
            formatted_price = "{:,.0f}".format(discounted_price).replace(",", ",")
            return "Rp " + formatted_price
        else:
            formatted_price = "{:,.0f}".format(self.price).replace(",", ",")
            return "Rp " + formatted_price



def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = Course.objects.filter(slug=slug).order_by('-id')
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" % (slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug


def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug and not instance.pk:
        instance.slug = create_slug(instance)

pre_save.connect(pre_save_post_receiver, sender=Course)

class what_you_learn(models.Model):
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    points = models.CharField(max_length=500)


    def __str__(self):
        return self.points

class Requirements(models.Model):
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    points = models.CharField(max_length=500)

    def __str__(self):
        return self.points

class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name + " - " + self.course.title


class Video(models.Model):
    serial_number = models.IntegerField(null=True)
    thumbnail = models.ImageField(upload_to="Yt_Thumbnail/",null=True)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson,on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
    youtube_id = models.CharField(max_length=500, null=True)
    time_duration = models.FloatField(null=True)
    preview = models.BooleanField(default=False)


    def __str__(self):
        return self.title

class UserCourse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    watched_videos = models.ManyToManyField(Video, blank=True)  # New field
    verified = models.BooleanField(default=False)
    paid = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.course.title}"

    def watched_percentage(self):
        total_videos = self.course.video_set.count()  # Total videos in the course
        watched_videos = self.watched_videos.count()  # Watched videos by the user

        if total_videos > 0:
            return (watched_videos / total_videos) * 100  # Percentage of watched videos
        else:
            return 0


class Order(models.Model):
    PAYMENT_STATUS = (
        ('Pending', 'Pending'),
        ('Complete', 'Complete'),
        ('Failed', 'Failed'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    payment_status = models.CharField(max_length=20, choices=PAYMENT_STATUS, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id}"

class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    transaction_id = models.CharField(max_length=255, null=True)
    amount = models.FloatField(null=True)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        if self.order is not None:
            return f'Payment for order {self.order.id}'
        else:
            return 'Payment with no associated order'

class UserVideoWatch(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    watched = models.BooleanField(default=False)

    class Meta:
        unique_together = ("user", "video")

    def __str__(self):
        return f"{self.user.username} - {self.video.title}"

    def mark_watched(self):
        self.watched = True
        self.save()

class UserCourseProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    progress = models.FloatField(default=0.0)  # Progres dalam persen
    last_accessed = models.DateTimeField(auto_now=True)  # Waktu terakhir pengguna mengakses kursus

    def watched_percentage(self):
        return self.progress

