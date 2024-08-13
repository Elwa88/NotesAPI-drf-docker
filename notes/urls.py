from django.urls import path
from .views import NoteListCreate, NoteUpdateDestroy

urlpatterns = [
    path('notes/',NoteListCreate.as_view()),
    path('notes/<int:pk>',NoteUpdateDestroy.as_view())

]
