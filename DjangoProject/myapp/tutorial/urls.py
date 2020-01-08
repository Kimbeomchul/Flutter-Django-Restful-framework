from django.contrib import admin
from django.urls import path
from django.conf.urls import url ,include
from main.views import CreateAPIView ,LoginAPIView  ,Logout , boardViewSet , commentViewSet
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token
from rest_framework_jwt.views import verify_jwt_token
from rest_framework.routers import DefaultRouter
from rest_framework import routers, serializers ,viewsets

router = routers.DefaultRouter()
router.register(r'posting',boardViewSet)
router.register(r'comment',commentViewSet)

urlpatterns = [

    path('admin/', admin.site.urls),
    url(r'^',include(router.urls)),
    url(r'^api-token-auth/', obtain_jwt_token), #Token
    url(r'^register/', CreateAPIView.as_view(),name='register'),
    url(r'^login/', LoginAPIView.as_view(),name='login'),
    url(r'^logout/', Logout.as_view()),
    url(r'^post/', boardViewSet),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
