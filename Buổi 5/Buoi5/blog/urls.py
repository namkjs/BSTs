from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.home),
    path('create',views.create_blog),
    path('read', views.table),
    path('update', views.update_blog),
    path('delete/<int:id>',views.delete_blog,name="delete"),
    path('view/<int:id>', views.read_blog),
    path('view/<int:id>',views.view_blog,name="view"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += staticfiles_urlpatterns()