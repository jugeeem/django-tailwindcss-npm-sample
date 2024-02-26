from django.contrib import admin
from django.urls import path
from sample.views import index

urlpatterns = [
    path("", index, name="index"), # 追記
    path("admin/", admin.site.urls),
]
