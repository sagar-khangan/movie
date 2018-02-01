"""movie URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from rest_framework import routers
from movieapp.views import MovieViewSet,DirectorViewSet,GenreViewSet,MoviePublicViewSet
from rest_framework.authtoken import views as rest_framework_views

router = routers.SimpleRouter()

router.register(r'movie', MovieViewSet)
router.register(r'director', DirectorViewSet)
router.register(r'genere', GenreViewSet)

public_router  = routers.SimpleRouter()

public_router.register((r'movie'),MoviePublicViewSet)



urlpatterns = [
    url(r'^api/admin/', admin.site.urls),
    url(r'^api/rest/', include(router.urls)),
    url(r'^api/public/', include(public_router.urls)),
    url(r'^api/get_auth_token/$', rest_framework_views.obtain_auth_token, name='get_auth_token'),
]
