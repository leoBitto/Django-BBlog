from django.conf import settings
from django.urls import path
from .views import views

app_name = 'BBlog'
urlpatterns = [

    path('articles/', views.articleListView, name="articles"),
    path('<slug:slug>/', views.articleView, name='article'),
]