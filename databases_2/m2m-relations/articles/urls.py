from django.contrib import admin

from django.urls import path

from articles.views import articles_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', articles_list, name='articles'),

]
