from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
urlpatterns = [
   path("", views.home, name="home-page"),
   path("topic/<slug:name>", views.category_threads , name = "category-threads"),
   path("topic/<slug:name>/create", views.create_thread , name = "create-threads"),
   path("thread/<slug:slug>", views.single_thread, name="single-thread")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)