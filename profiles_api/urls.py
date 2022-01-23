from django.urls import path, include
from rest_framework.routers import DefaultRouter
from profiles_api import views


# This is how you register ViewSets
router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')
router.register('profile', views.UserProfileViewSet)
router.register('feed', views.UserProfileFeedViewSet)


# This is how typical views are set
urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
    path('login/', views.UserLoginApiView.as_view()),
    path('', include(router.urls)), # This will generate views based upon the patterns of the viewsets (list, create, etc.) 
]