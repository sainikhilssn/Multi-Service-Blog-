from django.urls import path
from . import views
urlpatterns = [
    path('' , views.blogs_get_post , name = "blogs_get_post"),
    path('/<int:id>' , views.blogs_put_delete, name = "blogs_put_delete"),
    path('/search',views.blogs_search , name = 'blogs_search')
]

