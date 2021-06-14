from django.urls import path
from . import views

urlpatterns = [
    path('', views.ideas),
    path('add', views.add),
    path('<int:idea_id>', views.idea_detail),
    path('<int:idea_id>/delete', views.delete),
    path('<int:idea_id>/like', views.like),
    path('<int:idea_id>/unlike', views.unlike),
]