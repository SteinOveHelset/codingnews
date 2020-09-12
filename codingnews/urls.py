from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views

from apps.story.views import frontpage, search, submit, newest, vote, story
from apps.core.views import signup

urlpatterns = [
    path('', frontpage, name='frontpage'),
    path('s/<int:story_id>/vote/', vote, name='vote'),
    path('s/<int:story_id>/', story, name='story'),
    path('u/', include('apps.userprofile.urls')),
    path('newest/', newest, name='newest'),
    path('search/', search, name='search'),
    path('submit/', submit, name='submit'),
    path('signup/', signup, name='signup'),
    path('login/', views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('admin/', admin.site.urls),
]
