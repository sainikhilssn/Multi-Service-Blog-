from django.urls import path
from . import views

urlpatterns = [
    path('add' , views.reactions_post , name = "reactions_post"),
    path('delete/<int:id>' , views.reaction_delete , name = "reaction_delete")
]
