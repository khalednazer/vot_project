from . import views
from django.urls import path, include
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static

rot = routers.DefaultRouter()
rot.register('one', views.ViwSer)
urlpatterns = [
    path('one', views.show, name='onee' ),
    path('new/', include(rot.urls)),
    path('vot/',views.vot, name='voot')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

