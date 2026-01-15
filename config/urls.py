from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('panel/admin/', admin.site.urls),
    path('api/', include('core.urls'))
]
