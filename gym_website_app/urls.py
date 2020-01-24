from django.urls import path, re_path
from .views import index, signup_login, validate_username, user_logout

app_name = 'gym_website_app'

urlpatterns = [
    re_path(r'^$', index, name='home'),
    path('index/', index, name='index'),
    path('signup_login/', signup_login, name='signup & login'),
    path('login/', signup_login, name='login'),
    path('validate_uname', validate_username, name='validate_uname'),
    path('logout/', user_logout, name='logout user')
]
