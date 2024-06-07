from django.urls import include, path

from . import views

app_name="news_site"

urlpatterns = [
    path(
        "",
        views.HomePageView.as_view(),
        name="home",
    ),
]
