from django.urls import path
from .import views
app_name = 'account'

urlpatterns = [
    path('', views.loginUser),
    path('forgot-password/', views.forgotPass, name = 'forgotPass'),
    path('checkGmail/', views.checkGmail, name = 'checkGmail'),
    path('postloginUser/', views.postloginUser, name = 'postloginUser'),
]