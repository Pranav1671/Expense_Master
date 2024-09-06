from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('specific',views.specific,name='specific'),
    path('returndatas',views.returndatas,name='returndatas'),

    path('article/<int:article_id>',views.article,name='article'),
    path('article2/<int:article_id>',views.article2,name='article2'),
    path('new',views.new,name='new'),
]