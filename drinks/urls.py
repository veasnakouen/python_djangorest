"""
URL configuration for drinks project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from . import views
from rest_framework.urlpatterns import format_suffix_patterns #type:ignore
from rest_framework import routers #type:ignore

# *******************************
router = routers.SimpleRouter()
router.register('posts_list_view',views.PostViewSet,basename='post')#for ViewSet
router.register('posts_list_views',views.PostViewSets,basename='posts') #fore GenericViewSet
# *******************************


# *******************************
urlpatterns = [
    path('admin/', admin.site.urls),
    path('drinks/',views.drink_list),
    path('drinks/<int:id>',views.drink_details),

    # Post
    path('posts/',views.post_lists),
    path('details/<int:pk>',views.post_details),
    # Post with Class-based Views
    path('posts_class_view/',views.PostsAPIView.as_view()),
    path('details_class_view/<int:pk>',views.PostsDetailAPIView.as_view()),
    
    # generics + Mixins
    path('post_generic_list/<int:id>/',views.genericApiView.as_view()),
    
    # viewsets and Generic viewsets
    path('',include(router.urls)),
]
# *******************************


urlpatterns = format_suffix_patterns(urlpatterns)