from teamsite.settings import STATIC_ROOT
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('' , views.home),
]
urlpatterns+=static(settings.STATIC_URL,documnet_root = STATIC_ROOT)

urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)