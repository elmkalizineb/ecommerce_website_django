
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import Item


def item_list(request):
    context = {
        'items' : Item.objects.all()
    }

    return render(request, "item_list.html",context)