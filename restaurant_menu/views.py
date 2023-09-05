from django.shortcuts import render
from django.views import generic
from .models import Item, MEAL_TYPE


# Create your views here.

class MenuList(generic.ListView):
    queryset = Item.objects.order_by("meal")
    template_name = "index.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["meals"] = MEAL_TYPE
        return context
class MenuItemDetail(generic.DetailView):
    model = Item
    template_name = "menu_item_detail.html"

class About(generic.ListView):
    # queryset = Item.objects.order_by("meal")
    template_name = "about.html"

    # get query set override
    def get_queryset(self):
        queryset = super().get_queryset()
        term = self.kwargs.get('term')
        if term:
            return queryset.filter(body__icontains=term)
        return queryset.none()