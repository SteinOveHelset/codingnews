from django.urls import path

from .views import userprofile, votes, submissions

urlpatterns = [
    path('<str:username>/', userprofile, name='userprofile'),
    path('<str:username>/votes/', votes, name='votes'),
    path('<str:username>/submissions/', submissions, name='submissions'),
]