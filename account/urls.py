from django.urls import path
from account.views import register , login , profile , logout

urlpatterns = [
    path('register' , register , name="register"),
    path('login' , login , name="login"),
    path('' , profile , name="profile"),
    path('profile' , profile , name="profile"),
    path('logout' , logout , name="logout")
]