from django.urls import path
from .views import login, signup, logout, login_verify, signup_verify


urlpatterns = [
    path('login/', login, name='login'),
    path('signup/', signup, name='signup'),
    path('logout/', logout, name='logout'),
    path('login/verify/', login_verify),
    path('signup/verify/', signup_verify),
]
