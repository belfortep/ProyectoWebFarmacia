from django.urls import path

from . import views
from django.contrib.auth.views import LoginView, LogoutView

#enlazar urls del proyecto al de la aplicacion

urlpatterns = [
    
    
    path('login/', LoginView.as_view(template_name='login/login.html'), name='Login' ),
    path('logout/', LogoutView.as_view(template_name='login/logout.html'), name='Logout' ),

   


]