from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('login_and_reg', views.logreg),
    path('logout', views.logout),
    path('users/<int:user_id>', views.user)
]