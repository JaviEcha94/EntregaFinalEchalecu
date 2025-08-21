from django.urls import path
from .views import register, SimpleLoginView, SimpleLogoutView, profile, edit_profile

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', SimpleLoginView.as_view(), name='login'),
    path('logout/', SimpleLogoutView.as_view(), name='logout'),
    path('profile/', profile, name='profile'),
    path('profile/edit/', edit_profile, name='edit_profile'),
]
