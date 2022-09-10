from django.urls import include, path 
from rest_framework import routers
from todo import views
from todo.views import Logout, LogoutAllView, MyObtainTokenPairView, RegisterView
from rest_framework_simplejwt.views import TokenRefreshView
from . import views
from django.contrib.auth import views as auth_views



router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path(r'', include(router.urls)),
    path('login/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),

    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('reg/', RegisterView.as_view(), name='auth_register'),
    path('logout/', Logout.as_view() , name='user-logout'),
    path('logout_all/', LogoutAllView.as_view(), name='auth_logout_all'),
    
]

#url pattrens 