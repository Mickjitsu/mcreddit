from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
urlpatterns = [
   path("", views.home, name="home-page"),
   path("topic/<slug:name>", views.category_threads , name = "category-threads"),
   path("topic/<slug:name>/create", views.create_thread , name = "create-threads"),
   path("thread/<slug:slug>", views.single_thread, name="single-thread"),
   path("thanks", views.approval, name="pending"),
   path('thread/<slug:slug>/upvote/', views.upvote_thread, name='upvote_thread'),
   path('thread/<slug:slug>/downvote/', views.downvote_thread, name='downvote_thread'),
   path('comment/<int:comment_id>/upvote/', views.upvote_comment, name='upvote_comment'),
   path('comment/<int:comment_id>/downvote/', views.downvote_comment, name='downvote_comment'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)