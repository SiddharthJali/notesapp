from django.urls import path
from .views import NoteListView, NoteCreateView, NoteUpdateView, NoteDetailView, NoteDeleteView
from . import views

urlpatterns = [
    path('', NoteListView.as_view(), name='home'),
    # path('note/<int:note_id>/', views.note_detail, name='note-detail'),
    path('note/<int:pk>/', NoteDetailView.as_view(), name='note-detail'),
    path('note/new/', NoteCreateView.as_view(), name='note-create'),
    path('note/<int:pk>/update/', NoteUpdateView.as_view(), name='note-update'),
    path('note/<int:pk>/delete/', NoteDeleteView.as_view(), name='note-delete'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]
