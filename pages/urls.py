from django.urls import path

from . import views

app_name = 'pages'

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('cat/<int:cat>/', views.HomePageView.as_view(), name='home_cat'),
    path('cat/<int:cat>/sub/<int:sub>/', views.HomePageView.as_view(), name='home_sub'),
]
