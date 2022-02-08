from django.contrib import admin
from django.urls import path
from app.views import home ,login ,signup,logout,add_todo, delete_todo, change_todo
from django.contrib.auth.forms import UserCreationForm


urlpatterns = [
    path('', home , name='home'),
    path('login/', login, name='login'),
    path('signup/', signup,name='signup'),
    path('add-todo/', add_todo),
    path('delete-todo/<int:id>', delete_todo),
    path('change-status/<int:id>/<str:status>', change_todo),
    path('logout/', logout, name='logout'),



]
