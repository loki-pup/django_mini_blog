from django.urls import path
from . import views

urlpatterns = [
    path('blogs/', views.PostListView.as_view(), name='blogs'),
]
