from django.urls import path
from .import views

urlpatterns = [
    path("notes/",views.notes,name="notes"),
    path("notes/<slug:slug>/",views.note_detail,name="note_detail"),
    path("notes-search/",views.search_notes,name="search_notes"),
]

#endpoints:
#GET_ALL_NOTES_and_CREATE_NEW_NOTE = "127.0.0.1:8000/notes/"
#GET_SPECIFIC_NOTE = "127.0.0.1:8000/notes/note-slug"