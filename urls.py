from django.conf import settings
from django.urls import path
from .views import views
#from django.conf.urls.static import static

app_name = 'BBlog'
urlpatterns = [

    path('articles', views.articleListView, name="articles"),
    path('articles/<slug:slug>', views.articleView, name='article'),
]