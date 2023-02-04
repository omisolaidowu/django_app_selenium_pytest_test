from django.urls import path
from . import views


urlpatterns = [
	path('', views.home, name='home'),
	path('engine/<int:user_id>/', views.engine, name='engine'),
	path('eachpost/<slug:slug>/', views.eachpost, name='eachpost'),
	path('postlist/', views.postlist, name='postlist'),
	path('edit_post/<int:pk>-<int:user_id>/', views.edit_post, name='edit_post'),
	path('delete/<int:pk>/', views.delete_post, name='delete_post'),
	path('userlist/<int:user_id>/', views.userlist, name='userlist'),
	path('login/',  views.login, name='login'),
	path('register/',  views.register, name='registeration'),
	path('logout/',  views.logout, name='logout'),
	path('catlist/', views.catlist, name='catlist'),




	]
