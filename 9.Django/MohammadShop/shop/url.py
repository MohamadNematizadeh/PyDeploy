from django.urls import path
from .views import index, signup_view, signin_view, signout_view, profile_view  # اصلاح ایمپورت‌ها

urlpatterns = [
    path('', index, name="index"),
    path('signup/', signup_view, name='signup'),
    path('signin/', signin_view, name='signin'),
    path('signout/', signout_view, name='signout'),
    path('profile/', profile_view, name='profile'),
]
