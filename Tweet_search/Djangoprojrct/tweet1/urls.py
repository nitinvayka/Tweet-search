from django.urls import path
from . import views



urlpatterns = [
    path('', views.tweet_list, name='tweet_list'), 
    path('create/', views.tweet_create, name='tweet_create'), 

    path('<int:tweet_id>/edit/', views.tweet_edit, name='tweet_edit'), 
    path('<int:tweet_id>/delete/', views.tweet_delete, name='tweet_delete'), 
    path('register/', views.register, name='register'), 
    path('search/', views.search_tweets, name='tweet_search'),  # Add search URL
    path('search_results/', views.search_tweets, name='search_results'),  # Add search results URL
    path('result/', views.search_tweets, name='tweet_search'),  # Add results URL

    




] 