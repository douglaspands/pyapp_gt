from django.urls import path

from www.views.home import HomeView

app_name = "home"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
]
