from django.urls import path
from django.contrib.auth import views as auth_views
from usuario.views import new_usuario, LogoutGetView

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(
        template_name='usuario/login.html'
    ), name='login'),

    path('logout/', LogoutGetView.as_view(), name='logout'),


    path('new_usuario/', new_usuario, name='new_usuario'),
]