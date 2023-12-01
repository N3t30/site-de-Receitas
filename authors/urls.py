from django.urls import path

from . import views

app_name = 'authors'


urlpatterns = [
    path('register/', views.register_view, name='register'),  # register = view
    # R.creat = view que recebe os dados dos POST
    path('register/create/', views.register_create, name='register_create'),
    path('login/', views.login_view, name='login'),
    path('login/create/', views.login_create, name='login_create'),
    path('logout/', views.logout_view, name='logout'),
]
