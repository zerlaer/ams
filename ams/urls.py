from django.contrib import admin
from django.urls import path

import apps.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', apps.views.index),
    path('dashboard/', apps.views.dashboard),
    path('register/', apps.views.register),
    path('getassets/', apps.views.getassets)
]
