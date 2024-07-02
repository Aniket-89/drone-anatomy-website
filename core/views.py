from django.shortcuts import redirect, render
from django.utils import translation
from django.http import HttpResponseRedirect
from django.conf import settings
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


def set_language(request):
    user_language = request.GET.get('language', 'en')
    translation.activate(user_language)
    response = HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    response.set_cookie(settings.LANGUAGE_COOKIE_NAME, user_language)
    return response
