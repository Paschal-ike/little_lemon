from django.shortcuts import render, get_object_or_404
from .forms import BookingForm
from .models import *


# Create your views here.
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def book(request):
    form = BookingForm
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'book.html', context)


def menu(request):
    menu_data = Menu.objects.all().order_by('name')
    main_data = {'menu': menu_data}
    print("Menu Data:", menu_data) 

    return render(request, 'menu.html', {'menu':main_data})


def display_menu(request, pk=None):
    menu_item = get_object_or_404(Menu, pk=pk) if pk else None
    return render(request, 'menu_item.html', {'menu_item': menu_item})
