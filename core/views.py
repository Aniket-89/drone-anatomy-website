from django.shortcuts import render


def index_view(request):

    return render(request, "core/index.html", context={})


def agri_view(request):
    return render(request, "core/agri-drone.html", context={})