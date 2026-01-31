from django.urls import path
from library.views import *

urlpatterns = [
    path('',loginpage,name='loginpage'),
    path('dashboard/',dashboard,name='dashboard'),
    path('login/',loginUser,name='login'),
    path('logout/',logoutUser,name='logout'),
    path('addbook/',addBook,name='addbook'),
     path('addstudent/',addstudent,name='addstudent'),
    path('addteacher/',addteacher,name='addteacher'),
    path('booklist/',booklist,name='booklist'),
    path('withdrawbook/',withdrawbook,name='withdrawbook'),
    path('withdrawlist/',withdrawlist,name='withdrawlist'),
    path('deletewithdrawlist/<int:id>',deletewithdrawlist,name='deletewithdrawlist'),
    path('return/<int:id>',returned,name='returned'),
    path('passwordchange/',passwordchange,name='passwordchange'),
    path('passwordforgot/',passwordforgot,name='passwordforgot'),



]
