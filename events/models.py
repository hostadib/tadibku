from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.utils.text import slugify
import datetime
from django.urls import reverse

class Categories(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def get_all_category(self):
        return Categories.objects.all().order_by('id')

class Event(models.Model):
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    location = models.CharField(max_length=255)
    region = models.CharField(max_length=255, null=True)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=200, unique=True, null=True, blank=True)
    cover_event = models.ImageField(upload_to='Cover_event/', blank=True)
    category = models.ForeignKey ( Categories, on_delete=models.CASCADE,  null=True )
    speaker = models.CharField(max_length=255, null=True)
    speaker_image = models.ImageField(upload_to='Speaker/', null=True)
    speaker_desc = models.CharField(max_length=500, null=True)
    text = RichTextField()
    price = models.DecimalField(max_digits=10, decimal_places=0, null=True, default=0)
    discount = models.IntegerField(null=True)
    total_slot = models.IntegerField(default=0)
    booked_slot = models.IntegerField(default=0)


    def __str__(self):
        return self.title

    def formatted_price(self):
        return f"Rp {self.price:,.0f}"

    def discounted_price(self):
        if self.discount:
            discount_amount = self.price * self.discount / 100
            discounted_price = self.price - discount_amount
            formatted_price = "{:,.0f}".format(discounted_price).replace(",", ",")
            return "Rp " + formatted_price
        else:
            formatted_price = "{:,.0f}".format(self.price).replace(",", ",")
            return "Rp " + formatted_price


    def get_absolute_url(self):
        return reverse("events:event_detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def time_remaining(self):
        now = timezone.now()
        event_time = datetime.datetime.combine(self.date, self.start_time)
        event_time = timezone.make_aware(event_time)

        # Periksa apakah waktu acara sudah berlalu
        if now >= event_time:
            remaining = {
                'days': 0,
                'hours': 0,
                'minutes': 0,
                'seconds': 0,
            }
        else:
            time_delta = event_time - now

            remaining = {
                'days': time_delta.days,
                'hours': time_delta.seconds // 3600,
                'minutes': (time_delta.seconds // 60) % 60,
                'seconds': time_delta.seconds % 60,
            }

        return remaining