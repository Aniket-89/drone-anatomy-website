from django.shortcuts import redirect, render
from django.utils import translation
from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .forms import ContactForm, SubscriberForm
from .models import Subscriber
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import urllib.parse


def index_view(request):

    return render(request, "core/index.html", context={})


def agri_view(request):
    return render(request, "core/agri-drone.html", context={})


def about_view(request):
    return render(request, "core/about.html", context={})


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Send email
            try:
                send_mail(
                    'Test Mail',
                    f'Name: {name}\nEmail: {email}\n\nMessage:\n{message}',
                    settings.DEFAULT_FROM_EMAIL,  # Or use email
                    ['admin@droneanatomy.com'],
                    fail_silently=True,
                )
                if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                    return JsonResponse({'success': True, 'message': 'Message sent successfully!'})
                  # Ensure the name here matches your URL pattern name
            except Exception as e:
                error_message = f'Error: {e}'
                if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                    return JsonResponse({'success': False, 'error': error_message})
                else:
                    return render(request, 'core/contact.html', {'form': form, 'error': error_message})
        else:
            errors = form.errors.as_json()
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'success': False, 'errors': errors})
            else:
                return render(request, 'core/contact.html', {'form': form, 'errors': form.errors})
    else:
        form = ContactForm()
        success = request.GET.get('success')
        return render(request, 'core/contact.html', {'form': form, 'success': success})
    

def whatsapp_redirect(request):
    phone_number = "918130589012"
    whatsapp_url = f"https://wa.me/{phone_number}"
    message = "Hello"
    encoded_message = urllib.parse.quote(message)
    whatsapp_url += f"?text={encoded_message}"
    return redirect(whatsapp_url)


@csrf_exempt
def subscribe_newsletter(request):
    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            # Save email to your database or integrate with email service
            Subscriber.objects.get_or_create(email=email)
            return JsonResponse({'success': True, 'message': 'Subscription successful!'})
        else:
            errors = form.errors.as_json()
            return JsonResponse({'success': False, 'errors': errors})
    return JsonResponse({'success': False, 'message': 'Invalid request'})


def set_language(request):
    user_language = request.GET.get('language', 'en')
    translation.activate(user_language)
    response = HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    response.set_cookie(settings.LANGUAGE_COOKIE_NAME, user_language)
    return response
