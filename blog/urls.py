from django.urls import path

from . import views


app_name = 'blog'

urlpatterns = [
    path('', views.article_list, name='article_list'),
    path('1', views.article1),
    path('2', views.article2),
    path('3', views.article3),
    path('4', views.article4),
    path('5', views.article5),
    path('6', views.article6),
    path('7', views.article7),
    path('8', views.article8),

]

