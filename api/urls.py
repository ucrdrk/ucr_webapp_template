from django.urls import include, path
from rest_framework import routers
from . import views
from django.contrib import admin

from django.conf.urls import url, include

router = routers.DefaultRouter()
router.register(r'foos', views.FooViewSet)




urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    #url(r'^',include('account.api.urls'))
]
