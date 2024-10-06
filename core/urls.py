from django.urls import path
from .views import HomePageView, SamplePageView
from django.contrib import admin

urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
    path('sample/', SamplePageView.as_view(), name="sample"),
    path('admin/', admin.site.urls),
]