from django.urls import path

from www.views.home import HomeView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
]
