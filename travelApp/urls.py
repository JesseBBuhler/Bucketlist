from django.urls import path
from .views import deleteHandler, indexPageView, updateHandler, viewPageView
from .views import addPageView, searchPageView, addHandler, searchHandler, deleteHandler, updateHandler

urlpatterns = [
    path("", indexPageView, name="index"),   
    path("add/", addPageView, name="add"),
    path("search/<int:code>", searchPageView, name="search"),
    path("view/<int:id>/", viewPageView, name="view"),
    path("addHandler/", addHandler, name="addHandler"),
    path("searchHandler/", searchHandler, name="searchHandler"),
    path("delete/<int:id>", deleteHandler, name="delete"),
    path("update", updateHandler, name="update"),
] 