from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views import generic
from django.views.generic import View
from .models import User


# Create your views here.

def index(request):
    context = {}
    return render(request, 'showcase.html', context)


def item_new(request):
    context = {}
    return render(request, 'item_new.html', context)


class ShowcaseView(generic.ListView):
    template_name = 'showcase.html'
    context_object_name = 'dishes'  # <!-- default name: object_list -->


    def get_queryset(self):
        id = self.kwargs['seller_id']
        user = User.objects.get(id=11)
        return user.dish_set
