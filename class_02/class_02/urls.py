
from django.contrib import admin
from django.urls import path
from class_02.views import home_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home_page, name='home'),
]
