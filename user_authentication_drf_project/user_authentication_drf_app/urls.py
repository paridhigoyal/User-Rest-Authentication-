from django.conf.urls import re_path, url
from django.urls import include, path
from rest_auth.views import (LoginView, LogoutView, PasswordChangeView,
                             PasswordResetConfirmView, PasswordResetView,
                             UserDetailsView)
from rest_framework import routers

from . import views

# from .views import RegisterAPIView, UpdateAPIView
router = routers.DefaultRouter()
# router.register(r'register', views.RegisterViewSet)


urlpatterns = [
    path('', include(router.urls)),
    url(r'^password/reset/$', PasswordResetView.as_view(),
        name='rest_password_reset'),
    re_path(r'^password/reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
            PasswordResetConfirmView.as_view(),
            name='password_reset_confirm'),
    url(r'^login/$', LoginView.as_view(), name='rest_login'),
    url(r'^logout/$', LogoutView.as_view(), name='rest_logout'),
    url(r'^user/$', UserDetailsView.as_view(), name='rest_user_details'),
    url(r'^password/change/$', PasswordChangeView.as_view(),
        name='rest_password_change'),
    path('register', views.RegisterAPIView.as_view()),
    path('update', views.UpdateUserView.as_view()),
]
