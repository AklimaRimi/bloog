"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from app import views
from django.conf import settings
from django.conf.urls.static import static
from message import views as msgview

urlpatterns = [
    path('admin/', admin.site.urls),
    path('show-post/',views.showpost.as_view(),name = 'show-post'),
    path('show-one/<str:pk>/',views.detail.as_view(),name = 'show-one'),
    path('create',views.addpost.as_view(),name='create'),
    path('update/<str:pk>/',views.update.as_view(),name='update'),
    path('delete/<str:pk>/',views.delete.as_view(),name='delete'),
    path('members/', include('django.contrib.auth.urls')),
    path('registration/',views.registration.as_view(), name = 'registration' ),
    path('edit-profile/<str:pk>',views.UserEditForm.as_view(), name = 'edit-profile' ),
    path('<str:pk>/showprofile',views.showprofile.as_view(), name = 'showprofile'),
    
    path('login/',views.user_login, name = 'login' ),
    path('likeview/<str:pk>/',views.likeview,name='likeview'), 

    path('article/<str:pk>/comment',views.comment.as_view(),name='comment'),

    path('message/<str:pk>/',msgview.room, name = 'room'),   

]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
