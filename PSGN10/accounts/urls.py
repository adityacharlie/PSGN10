from django.urls import path

from . import views

urlpatterns = [
	path('auth/user/', views.UserInfo.as_view(), name='user_infos'),
    path('login/', views.Login.as_view(), name='login'),
    path('user-type/', views.user_type, name='user_type'),
    path('logout/', views.Logout.as_view(), name='logout'),
]
