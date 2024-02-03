import midtransclient
from django.shortcuts import render, redirect, get_object_or_404
from app.models import Video, Categories, Course, Level, UserCourse, Payment, Order, Author, UserVideoWatch, UserCourseProgress
from django.template.loader import render_to_string
from django.http import JsonResponse, Http404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.urls import reverse
import random
from artikel.models import ArtikelPost, Post
from events.models import Event
from django.db.models import Count




def BASE(request):
    return render(request, 'base.html')

def HOME(request):
    category = Categories.objects.all().order_by('id')[0:5]
    course = Course.objects.filter(status='PUBLISH').order_by('-id')
    artikel = ArtikelPost.objects.all().order_by('date_posted')[0:3]
    events = Event.objects.all().order_by('date')[0:3]


    context = {
        'category': category,
        'course': course,
        'artikel': artikel,
        'events': events



    }
    return render(request, 'main/home.html' , context)

def SINGLE_COURSE(request):
    category = Categories.get_all_category(Categories)
    level = Level.objects.all()
    course = Course.objects.all()
    freecourse = Course.objects.filter(price=0).count()
    paidcourse = Course.objects.filter(price__gte=1).count()
    context = {
        'category': category,
        'level': level,
        'course': course,
        'freecourse': freecourse,
        'paidcourse': paidcourse,
    }

    return render(request, 'main/single_course.html', context)

def FILTER_DATA(request):
    category = request.GET.getlist('category[]')
    level = request.GET.getlist('level[]')
    price = request.GET.get('price[]')

    if price == ['pricefree']:
        course = Course.objects.filter(price=0)
    elif price == ['pricepaid']:
        course = Course.objects.filter(price__gte=1)
    elif price == ['priceall']:
        course = Course.objects.all()
    elif category:
        course = Course.objects.filter(category__id__in=category).order_by('-id')
    elif level:
        course = Course.objects.filter(level__id__in=level).order_by('-id')
    else:
        course = Course.objects.all().order_by('-id')

    context = {
        'course': course,
    }

    t = render_to_string('ajax/course.html', context)
    return JsonResponse({'data': t})


def CONTACT_US(request):
    category = Categories.get_all_category(Categories)
    context = {
        'category': category,
    }
    return render(request, 'main/contact_us.html', context)

def ABOUT_US(request):
    category = Categories.get_all_category(Categories)
    context = {
        'category': category,
    }
    return render(request, 'main/about_us.html', context)

def guru_list(request):
    authors = Author.objects.all()
    context = {
        'authors': authors,
    }
    return render(request, 'main/guru_list.html', context)

def guru_detail(request, author_id):
    author = get_object_or_404(Author, pk=author_id)

    context = {
        'author': author
    }
    return render(request, 'main/guru_detail.html', context)

def SEARCH_COURSE(request):
    query = request.GET['query']
    course = Course.objects.filter(title__icontains = query)
    context = {
        'course':course,
    }
    return render(request,'search/search.html',context)


def get_all_category():
    return Categories.objects.all().order_by('id')

@login_required(login_url='login')
def COURSE_DETAIL(request, slug):
    category = get_all_category()
    authors = Author.objects.annotate(course_count=Count('course'))
    course = Course.objects.filter(slug=slug).first()

    if not course:
        return redirect('404')

    user = request.user  # Menggunakan request.user langsung

    try:
        check_enroll = UserCourse.objects.filter(user=user, course=course).first()
    except UserCourse.MultipleObjectsReturned:
        check_enroll = None

    payment = Payment.objects.filter(user=user, course=course).first()
    if payment and payment.is_verified:
        try:
            check_enroll = UserCourse.objects.filter(user=user, course=course).first()
        except UserCourse.MultipleObjectsReturned:
            check_enroll = None
    else:
        messages.error(request, "Pembayaran untuk kursus ini belum diverifikasi.")
        return redirect('home')

    context = {
        'course': course,
        'category': category,
        'check_enroll': check_enroll,
        'authors': authors,
    }
    return render(request, 'course/course_detail.html', context)



def PAGE_NOT_FOUND(request):
    return render(request, 'error/404.html')

def CHECKOUT(request, slug):
    course = Course.objects.get(slug=slug)
    category = Categories.get_all_category(Categories)
    action = request.GET.get('action')
    receipt = None

    if course.price == 0:
        course_user = UserCourse(
            user=request.user,
            course=course,
        )
        course_user.save()
        messages.success(request, 'Alhamdulillah anda berhasil mengikuti kelas ini')
        return redirect('mycourse')

    elif action == 'create_payment':
        if request.method == 'POST':
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            country = request.POST.get('country')
            address = request.POST.get('address')
            city = request.POST.get('city')
            zip_code = request.POST.get('zip_code')
            phone = request.POST.get('phone')
            email = request.POST.get('email')

            # Create a new Order instance
            order = Order(
                user=request.user,
                course=course,
            )
            order.save()

            # Create a new Payment instance
            payment = Payment(
                order=order,
                transaction_id=f'edutadib-{random.randint(10000, 99999)}'
            )
            print(payment.__dict__)
            payment.save()

            success_url = reverse('payment_success', args=[payment.id])
            return JsonResponse({'success_url': success_url})

    context = {
        'course': course,
        'category': category,
        'receipt': receipt,
    }
    return render(request, 'checkout/checkout.html', context)


def PAYMENT_SUCCESS(request, payment_id):
    payment = Payment.objects.get(id=payment_id)
    payment.status = False
    payment.save()

    UserCourse.objects.create(user=payment.order.user, course=payment.order.course)

    return render(request, 'checkout/success.html', {'transaction_id': payment.transaction_id})


@login_required(login_url='login')
def MYCOURSE(request):
    category = Categories.get_all_category(Categories)

    if request.user.is_authenticated:
        user_courses = UserCourse.objects.filter(user=request.user)
        course_count = user_courses.count()  # Count the courses
        courses = []
        for user_course in user_courses:
            course_info = {
                'course': user_course.course,
                'payment': Payment.objects.filter(user=request.user, course=user_course.course, is_verified=True).first(),
                'category': category,
            }

            # Dapatkan semua video dalam kursus ini
            course_videos = Video.objects.filter(course=user_course.course)

            # Dapatkan semua UserVideoWatch untuk pengguna ini dan video dalam kursus ini
            watched_videos = UserVideoWatch.objects.filter(user=request.user, video__in=course_videos, watched=True)

            # Hitung persentase dan simpan dalam dictionary course_info
            course_info['watched_percentage'] = (watched_videos.count() / course_videos.count()) * 100

            courses.append(course_info)
    else:
        courses = None  # or whatever makes sense in your context
        course_count = 0  # No courses if the user is not authenticated

    context = {
        'courses': courses,
        'category': category,
        'course_count': course_count,  # Add the count to the context
    }
    return render(request, 'course/mycourse.html', context)



def SAVE_PROGRESS(request, course_id):
    Course.objects.filter(id=course_id).update(progress=True)
    return redirect('course_detail', course_id=course_id)




@login_required(login_url='login')
def WATCH_COURSE(request, slug):
    try:
        course = Course.objects.get(slug=slug)
    except Course.DoesNotExist:
        return redirect('404')

    lecture = request.GET.get('lecture')
    video = None

    if lecture is not None:
        try:
            video_id = int(lecture)
            video = Video.objects.get(id=video_id)

            user_video_watch, created = UserVideoWatch.objects.get_or_create(user=request.user, video=video)
            if not created:
                user_video_watch.watched = True
                user_video_watch.save()

                total_videos = Video.objects.filter(course=course).count()
                if total_videos > 0:
                    watched_videos = UserVideoWatch.objects.filter(user=request.user, video__course=course,
                                                                   watched=True).count()
                    progress = (watched_videos / total_videos) * 100
                    UserCourseProgress.objects.update_or_create(user=request.user, course=course,
                                                                defaults={'progress': progress})

        except ValueError:
            raise Http404("Invalid video id")
        except Video.DoesNotExist:
            raise Http404("Video does not exist")

    watched_videos = UserVideoWatch.objects.filter(user=request.user, watched=True).values_list('video_id', flat=True)

    context = {
        'course': course,
        'video': video,
        'watched_videos': watched_videos,
    }

    return render(request, 'course/watch-course.html', context)



def VERIFY_PAYMENT(request, transaction_id):
    try:
        payment = Payment.objects.get(transaction_id=transaction_id)
    except Payment.DoesNotExist:
        raise Http404("Payment does not exist")

    if payment.status == 'Completed':
        # Create a new UserCourse instance
        user_course = UserCourse.objects.create(user=payment.user, course=payment.course)
        user_course.save()

        context = {'transaction_id': transaction_id, 'payment': payment, 'course': user_course}
        return render(request, 'success.html', context)
    else:
        context = {'transaction_id': transaction_id}
        return render(request, 'fail.html', context)

