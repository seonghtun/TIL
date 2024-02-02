from django.urls import path

from . import views

app_name = "burgers"
urlpatterns = [
    path("", views.main, name="main"),
    path("list/", views.burger_list, name="burger_lists"),
    path("search/", views.burger_search, name="burger_searchs"),
]