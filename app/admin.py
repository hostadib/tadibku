from django.contrib import admin
from .models import *

class what_you_learnInline(admin.TabularInline):
    model = what_you_learn


class RequirementsInline(admin.TabularInline):
    model = Requirements


class Vidio_TabularInline(admin.TabularInline):
    model = Video


class CourseAdmin(admin.ModelAdmin):
    inlines = [what_you_learnInline, RequirementsInline, Vidio_TabularInline]

class PaymentAdmin(admin.ModelAdmin):
    list_display = ['user', 'course', 'amount', 'is_verified']
    actions = ['verified_payment']

    def verified_payment(self, request, queryset):
        queryset.update(is_verified=True)
    verified_payment.short_description = "Mark selected payment as verified"


admin.site.register(Categories)
admin.site.register(Author)
admin.site.register(Course, CourseAdmin)
admin.site.register(Level)
admin.site.register(what_you_learn)
admin.site.register(Requirements)
admin.site.register(Lesson)
admin.site.register(Video)
admin.site.register(UserCourse)
admin.site.register(Payment, PaymentAdmin)


# Register your models here.
