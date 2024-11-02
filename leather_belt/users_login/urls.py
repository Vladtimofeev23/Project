from . import views
from django.contrib.auth.views import LogoutView
from django.urls import path

app_name = 'users_login'

urlpatterns = [
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', views.Register.as_view(), name='register'),
    # path('personal_area/<int:user_id>', views.user_view, name='personal_area'),
    path('personal_area/', views.profile, name='personal_area'),

]