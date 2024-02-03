
from .import views, user_login
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('logout', user_login.LOGOUT, name='logout'),
    path('base', views.BASE, name='base'),
    path('404', views.PAGE_NOT_FOUND, name='404'),
    path('', views.HOME, name='home'),
    path('courses', views.SINGLE_COURSE, name='single_course'),
    path('course/<slug:slug>', views.COURSE_DETAIL, name='course_detail'),
    path('contact' , views.CONTACT_US, name='contact_us'),
    path('tentang_tadib', views.ABOUT_US, name='tentang_tadib'),
    path('guru_list/', views.guru_list, name='guru_list'),
    path('guru_detail/<int:author_id>/', views.guru_detail, name='guru_detail'),

    path('courses/filter-data', views.FILTER_DATA, name='filter_data'),
    path('search',views.SEARCH_COURSE,name='search_course'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', user_login.REGISTER, name='register'),
    path('doLogin', user_login.DO_LOGIN, name='doLogin'),
    path('profile', user_login.PROFILE, name='profile'),
    path('accounts/profile/update', user_login.PROFILE_UPDATE, name='profile_update'),
    path('checkout/<slug:slug>', views.CHECKOUT, name='checkout'),
    path('checkout/success/<int:payment_id>/', views.PAYMENT_SUCCESS, name='payment_success'),

    path('mycourse', views.MYCOURSE, name='mycourse'),
    path('save_progress', views.SAVE_PROGRESS, name='save_progress'),
    path('course/watch-course/<slug:slug>', views.WATCH_COURSE, name='watch_course'),
    path('verify-payment', views.VERIFY_PAYMENT, name='verify_payment'),

    path('artikel/', include('artikel.urls')),
    path('events/', include('events.urls')),
    path('sekolah/',include('sekolah.urls')),




]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

