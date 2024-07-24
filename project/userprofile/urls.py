from django.urls import path

from .views import front_view,login_view,signup_view,logout_view,home_view,profile_view,update_user_profile,update_password_view

from .views import faq_view,contact_view,services_view


urlpatterns = [
    path('front/',front_view, name="front_view"),
    path('login/',login_view,name="login_view"),
    path('signup/',signup_view,name="signup_view"),
    path('logout/',logout_view,name="logout_view"),
    path('home/',home_view,name="home_view"),

    path('profile-view/<str:username>/',profile_view,name="profile_view"),
    path('update-user-profile/',update_user_profile,name="update_user_profile"),
    path('update-password-view/',update_password_view,name="update_password_view"),

    path('faq/', faq_view, name="faq"),
    path('contact/', contact_view, name="contact"),
    path('services/', services_view, name="services"),
    
]