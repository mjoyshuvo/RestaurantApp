from django.shortcuts import render


def home(request):
    title = 'Inventory'
    return render(request, 'home.html', {'title': title})
