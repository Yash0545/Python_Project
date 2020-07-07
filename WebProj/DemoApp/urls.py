from django.urls import path
from . import views
urlpatterns = [
    path('',views.hi,name='Home page'),
    path('Admin/',views.Admin,name='Admin Page')
]