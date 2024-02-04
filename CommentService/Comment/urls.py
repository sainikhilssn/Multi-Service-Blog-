from django.urls import path
from . import views
urlpatterns = [
    path('comments/blog/<int:id>' , views.blog_comments , name = "blogs_comments"),
    path('comments' , views.blog_add_comments, name = "blog_add_comment"),
    path('comments/<int:id>' , views.comments_get_put, name = "comment_get_put"),
    path('comments/blog/<int:id>/comments' , views.blog_delete_comments, name = "blog_delete_comment"),
]
