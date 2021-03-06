from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import include
from rest_framework import routers
from .views import UserViewSet, documentDetails
from api.views import documentApi
from api.views import usersApi

router = routers.DefaultRouter()
router.register('users', UserViewSet)

urlpatterns = [
    # path('', include(router.urls)),
    re_path(r'^form/(?P<id>[0-9a-f-]+)', documentDetails),
    re_path(r'get_all_forms', documentApi),
    re_path(r'users/', usersApi)
]