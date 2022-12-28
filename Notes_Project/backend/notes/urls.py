from django.urls import path, include

from . import views


urlpatterns = [

    path('notes', views.NotesListView.as_view()), 
    path('notes/<int:pk>', views.NotesDetailView.as_view()),
    
]