from django.urls import path
from .import views
urlpatterns=[
    path('',views.home,name="home"),
    path('about/',views.about,name="about"),
    path('menu/',views.menu,name="menu"),
    path('contact/',views.contact,name="contact" ),
    path('order/',views.order,name="oorder"),
    path('fun/',views.wet,name="fun"),
    path('OS/',views.os,name="os"),
    path('io/',views.show,name="show")
    # path('register/',views.details,name="register")

]