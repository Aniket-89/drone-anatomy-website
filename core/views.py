from django.shortcuts import redirect, render
import urllib.parse


def index_view(request):

    return render(request, "core/index.html", context={})


def agri_view(request):
    return render(request, "core/agri-drone.html", context={})


def about_view(request):
    return render(request, "core/about.html", context={})


def whatsapp_redirect(request):
    phone_number = "918130589012"
    whatsapp_url = f"https://wa.me/{phone_number}"
    message = "Hello"
    encoded_message = urllib.parse.quote(message)
    whatsapp_url += f"?text={encoded_message}"
    return redirect(whatsapp_url)
