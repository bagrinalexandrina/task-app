from django.conf.urls import include
from django.contrib import admin
from django.urls import path

from common.__init__ import schema_view


urlpatterns = [
    path("", schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('admin/', admin.site.urls),
    path('user/', include('users.urls')),
    path('tasks/', include('tasks.urls'))

]
