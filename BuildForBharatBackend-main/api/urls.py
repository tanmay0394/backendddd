from rest_framework_simplejwt import views as jwt_views
from django.urls import path
from . import views

urlpatterns = [
    path('register', views.UserRegisterView.as_view()),
    path('login', views.UserLoginView.as_view()),
    path('token/refresh', jwt_views.TokenRefreshView.as_view()),
    path('logout', jwt_views.TokenBlacklistView.as_view()),
    path('home', views.HomeView.as_view()),
    path('catalogue/create/', views.CatalogueCreateView.as_view(), name='catalogue-create'),
    path('catalogue/getDetails/', views.CatalogueDetailView.as_view(), name='catalogue-detail'),
    path('catalogue/uploadExistingCatalogue/', views.CatalogueUploadView.as_view(), name='catalogue-upload')

]
