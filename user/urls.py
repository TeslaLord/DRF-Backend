from django.urls import path, include
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

urlpatterns = [
    path('login/', views.LoginView.as_view()),
    path('register/', views.RegisterView.as_view()),
    path('users_list/', views.users_list),
    path('<int:pk_user>/advisor/',views.advisor_list),
    path('<int:pk_user>/advisor/<int:pk_advisor>/',views.book_advisor),
    path('<int:pk_user>/advisor/booking/',views.booked_calls),
    path('token/',TokenObtainPairView.as_view()),
    path('token/refresh',TokenRefreshView.as_view()),
    path('token/verify',TokenVerifyView.as_view()),
]
