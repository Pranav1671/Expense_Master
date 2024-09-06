from django.urls import path
from django.conf import settings
from . import views
# from django.conf.urls.static import static
from .views import create_user_profile
from .views import save_user_profile

urlpatterns = [
    path('openweb',views.openweb,name='openweb'),
    path('my_expense_view', views.my_expense_view, name='my_expense_view'),
    path('open_html/', views.open_html, name='open_html'),
    path('save_user_profile/', views.save_user_profile, name='save_user_profile'),
    path('open_login/', views.open_login, name='open_login'),
    path('open_signup/', views.open_signup, name='open_signup'),
    path('create_user_profile/', create_user_profile, name='create_user_profile'),
    path('login/', save_user_profile, name='login'),
    path('loginpass/', views.loginpass, name='loginpass'),
    path('signuppass/', views.signuppass, name='signuppass'),
]