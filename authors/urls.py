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
    path('dashboard/', views.dashboard, name='dashboard'),
    path(
        'dashboard/recipe/new/',
        views.DashboardRecipe.as_view(),
        name='dashboard_recipe_new',
    ),
    path(
        'dashboard/recipe/delete/',
        views.dashboard_recipe_delete,
        name='dashboard_recipe_delete'
    ),
    path(
        # dentro de toda classbased view
        #  tem um metodo que é chamado de as_view
        'dashboard/recipe/<int:id>/edit/',
        views.DashboardRecipe.as_view(),
        name='dashboard_recipe_edit',
    ),

]
