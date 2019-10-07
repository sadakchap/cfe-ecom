from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/',views.login_page,name='login'),
    path('logout/',views.logout_page,name='logout'),
    path('sign-up/',views.signup_page,name='signup'),
    path('my-profile/',views.my_profile,name='my-profile'),
]
