"""quanda URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from rest_framework.routers import DefaultRouter
from main_app.views import LogInViewSet, SignUpViewSet, UserViewSet


router = DefaultRouter()
router.register(r"login", LogInViewSet, basename="login")
router.register(r"signup", SignUpViewSet, basename="signup")
router.register(r"user", UserViewSet, basename="user")
urlpatterns = router.urls

DJANGO_MAIN_URL = "http://127.0.0.1:8000/"
REACT_MAIN_URL = "http://127.0.0.1:3000/"
