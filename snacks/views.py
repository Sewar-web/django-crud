from django.db import models
from django.shortcuts import render

from django.views.generic import ListView , DetailView,CreateView ,UpdateView,DeleteView

from .models import snacks

from django.urls import reverse_lazy




class SnackListView(ListView):
    template_name='snack_list.html'
    model=snacks


class SnackDetailView(DetailView):

    template_name='snack_view.html'
    model=snacks

class SnackCreateView(CreateView):

    template_name='snack_creat.html'
    model=snacks
    fields=['title', 'purchaser' ,'description']


class SnackUpdateView(UpdateView):

    template_name='snack_update.html'
    model=snacks
    fields=['title', 'purchaser' ,'description']

class SnackDeleteView(DeleteView):

    template_name='snack_delete.html'
    model=snacks
    success_url= reverse_lazy('snack_list')



