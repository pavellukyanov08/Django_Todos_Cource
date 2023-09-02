from django.contrib import admin
from django.urls import path
from todo import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Auth
    path('signup/', views.signupuser, name='signup'),
    # Logout
    path('lognout/', views.logoutuser, name='logout'),
    path('login/', views.loginuser, name='login'),

    # Todos
    path('', views.home, name='home'),
    path('currenttodos/', views.currenttodos, name='current'),
    path('create/', views.createtodo, name='create'),
    path('todo/<int:todo_pk>', views.viewtodo, name='viewtodo'),
    path('todo/<int:todo_pk>/complete', views.completetodo, name='complete'),
    path('todo/<int:todo_pk>/delete', views.deletetodo, name='delete'),
]
