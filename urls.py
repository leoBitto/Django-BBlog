from django.conf import settings
from django.urls import path
from .views import views
#from django.conf.urls.static import static

app_name = 'BBlog'
urlpatterns = [

    path('', views.articleListView, name="articles"),
    path('<slug:slug>', views.articleView, name='article'),
]