from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('create/',views.shopcreate,name='create'),
    path('contact/',views.contact,name='contact'),
    path('categories/',views.categories,name='categories'),
    path('checkout/',views.checkout,name='checkout'),
    path('shoe4/',views.shoe4,name='shoe4'),
    path('shoe3/',views.shoe3,name='shoe3'),
    path('shoe2/',views.shoe2,name='shoe2'),
    path('shoe1/',views.shoe1,name='shoe1'),
    path('dress1/',views.dress1,name='dress1'),
    path('dress2/',views.dress2,name='dress2'),
    path('dress3/',views.dress3,name='dress3'),
    path('dress4/',views.dress4,name='dress4'),
    path('bag1/',views.bag1,name='bag1'),
    path('bag2/',views.bag2,name='bag2'),
    path('bag3/',views.bag3,name='bag3'),
    path('bag4/',views.bag4,name='bag4'),
    path('acc1/',views.acc1,name='acc1'),
    path('acc2/',views.acc2,name='acc2'),
    path('acc3/',views.acc3,name='acc3'),
    path('acc4/',views.acc4,name='acc4'),
    path('about/',views.about,name='about'),

    path('thankyou/',views.thankyou,name='thankyou'),
    

    path('signup/',views.signup_view,name="signup"),
    path('login/',views.login_view,name='login'),
    path('logout/',views.logout_view,name='logout'),








    ]
