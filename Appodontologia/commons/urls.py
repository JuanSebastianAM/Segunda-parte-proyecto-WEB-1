from django.urls import path
from . import views
from .views import login_and_register
urlpatterns = [
    path('',views.index, name = 'index'),
  path('login/', login_and_register, name='login_and_register')

]