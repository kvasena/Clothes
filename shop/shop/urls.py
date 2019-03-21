from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('product/', include('pomazan_shop.urls')),
    path('admin/', admin.site.urls),
]
