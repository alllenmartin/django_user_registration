from django.urls import path, include
from .views import UserViewSet
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt import views as jwt_views

router = DefaultRouter()
router.register('users', UserViewSet)
urlpatterns = router.urls

urlpatterns = [
    path('', include(router.urls)),
    path('auth', jwt_views.TokenObtainPairView.as_view(), name='token_auth'),

]