from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
	#path('login/',views.LoginView.as_view(),name='login'),
    path('', views.index,name="index"),
    path('contact/',views.contact,name="contact"),
    path('signup/',views.signup,name="signup"),
    path('login/',views.login1,name="login1"),
    path('accounts/',include('django.contrib.auth.urls')),
    path('shimla/',views.shimla,name="shimla"),
    path('kinnaur/',views.kinnaur,name="kinnaur"),
    path('dalhousie/',views.dalhousie,name="dalhousie"),
    path('dharamshala/',views.dharamshala,name="dharamshala"),
    path('spiti/',views.dalhousie,name="spiti"),
    path('manali/',views.manali,name="manali"),
    path('logout/',views.logout1,name="logout"),
    path('booking/<str:title>/<str:title1>/<str:title2>',views.booking,name="booking"),
    path('customization/<str:title>/',views.customization,name="customization"),
    path('customize/<str:title>/<int:number>',views.customize,name="customize"),
    path('previous_booking/<str:name>/',views.previous_booking,name="previous"),
]