from django.urls import path
from . import views
urlpatterns=[
  path('',views.home,name='home'),
  path('signup',views.signup,name="signup"),
  path('login',views.login_page,name="login"),
  path('logout',views.logout_page,name="logout"),
  path('profile/', views.profile, name='profile'),
  path('profile/delete/<int:id>/',views.delete,name='delete'),
   path('profile_edit/', views.profile_edit, name='profile_edit'),
   path('posts/new/', views.create_post, name='post_create'),
   path('search',views.search_profile,name="searchs"),
   path('profile/<int:id>/', views.profile_view, name='profile_view'),
 ]