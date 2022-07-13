from django.urls import path,include
from . import views
urlpatterns = [
   path("",views.IndexPage,name="index"),
   path("signup/",views.singupPage,name="signup"),
   path("register/",views.RegisterUser,name="register"),
   path("otppage/",views.OTPPage,name="otppage"),
]