from django.contrib import admin
from django.urls import path
from myproject.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', loginpage, name='loginpage'),
    path('base', base, name='base'),
    path('home', home, name='home'),
    path('table', table, name='table'),
    path('teacher', teacher, name='teacher'),
    path('cource', cource, name='cource'),
    path('calender', calender, name='calender'),
    path('library', library, name='library'),
    path('result', result, name='result'),
    path('shedeul', shedeul, name='shedeul'),
    path('batch', batch, name='batch'),
    path('semester', semester, name='semester'),
    path('section', section, name='section'),
    path('classes', classes, name='classes'),
    path('password_change', password_change, name='password_change'),
    path('registerpage/', registerpage, name='registerpage'),
    path('logoutpage/', logoutpage, name='logoutpage'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
