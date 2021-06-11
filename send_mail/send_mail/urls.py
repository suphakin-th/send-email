from django.conf.urls import url
from django.contrib import admin
from django.urls import path

from send_mail.views import SendMailViews

urlpatterns_email = [
    url('api/send_mail', SendMailViews.as_view(), name='send_mail'),
]

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += urlpatterns_email
