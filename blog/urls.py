from django.urls import path, include
from django.contrib.auth import views as auth_views

from blog import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blog/<tag>/', views.index, name='category_tag'),
    path('home/', views.create_post_view, name='home'),
    path('event/<int:pk>/', views.post_detail_view, name='post_detail'),
    path('post/<int:pk>', views.add_comment_to_post, name='add_comment_to_post'),
    path('accounts/', include("django.contrib.auth.urls")),
    path('register/', views.register, name='register')

]
