from django.forms.models import BaseModelForm
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Note


@login_required
def home(request):
    context = {
        'notes': Note.objects.all()
    }
    return render(request, 'notes/home.html', context)


class NoteListView(LoginRequiredMixin, ListView):
    model = Note
    template_name = 'notes/home.html'
    context_object_name = 'notes'


class NoteDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Note

    def test_func(self):
        note = self.get_object()
        if self.request.user == note.author:
            return True
        return False


class NoteCreateView(LoginRequiredMixin, CreateView):
    model = Note
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class NoteUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Note
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        note = self.get_object()
        if self.request.user == note.author:
            return True
        return False


class NoteDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Note
    success_url = '/'

    def test_func(self):
        note = self.get_object()
        if self.request.user == note.author:
            return True
        return False

# @login_required
# def note_detail(request, note_id):
#     specific_note = get_object_or_404(Note, id=note_id)
#     all_notes = Note.objects.all

#     context = {
#         'specific_note': specific_note,
#         'all_notes': all_notes,
#     }

#     return render(request, 'notes/note_detail.html', context)


def about(request):
    return render(request, 'notes/about.html', {'title': 'about.'})


def contact(request):
    return render(request, 'notes/contact.html', {'title': 'contact.'})
