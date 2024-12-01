from django.urls import path
from . import views
urlpatterns = [
   path("", views.home, name="home-page"),
   path("topic/<slug:name>", views.category_threads , name = "category-threads")
]