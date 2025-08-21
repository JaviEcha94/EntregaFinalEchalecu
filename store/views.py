from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from .models import Game
from .forms import GameForm

class GameListView(ListView):
    model = Game
    template_name = 'store/game_list.html'
    context_object_name = 'games'

    def get_queryset(self):
        qs = super().get_queryset().order_by('-id')
        q = self.request.GET.get('q') or ''
        if q:
            qs = qs.filter(Q(title__icontains=q) | Q(genre__icontains=q) | Q(rating__icontains=q))
        return qs

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['q'] = self.request.GET.get('q') or ''
        return ctx

class GameDetailView(DetailView):
    model = Game
    template_name = 'store/game_detail.html'
    context_object_name = 'game'

class GameCreateView(LoginRequiredMixin, CreateView):
    model = Game
    form_class = GameForm
    template_name = 'store/game_form.html'
    success_url = reverse_lazy('store:game_list')

class GameUpdateView(LoginRequiredMixin, UpdateView):
    model = Game
    form_class = GameForm
    template_name = 'store/game_form.html'
    success_url = reverse_lazy('store:game_list')

class GameDeleteView(LoginRequiredMixin, DeleteView):
    model = Game
    template_name = 'store/game_confirm_delete.html'
    success_url = reverse_lazy('store:game_list')
