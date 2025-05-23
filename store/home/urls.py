from django.urls import path
from .import views

urlpatterns=[
    path('',views.home,name='home'),
    path('login/',views.login_user,name='login'),
    path('logout/',views.logout_user,name='logout'),
    path('register/',views.register_user,name='register'),
    path('product/<str:product_name>/', views.product, name='product'),
    path('mobiles/<str:cat>/', views.mobiles, name='mobiles'),
]