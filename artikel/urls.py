from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import ArtikelPostCreateView

app_name = 'artikel'

urlpatterns = [
    path('', views.artikel_list, name='artikel_list'),
    path('<slug:slug>', views.artikel_detail, name='artikel_detail'),  # This is for artikel
    path('artikel/new/', ArtikelPostCreateView.as_view(), name='artikel_new'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)