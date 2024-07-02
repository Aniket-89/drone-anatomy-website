from django.conf import settings
from django.http import HttpResponsePermanentRedirect

class WWWRedirectMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check if the request's host is non-www and not on HTTPS
        if settings.DEBUG:  # Optional check to avoid redirection in debug mode
            return self.get_response(request)

        if request.META['HTTP_HOST'] == 'droneanatomy.com' and not request.is_secure():
            redirect_url = 'https://www.droneanatomy.com' + request.path
            return HttpResponsePermanentRedirect(redirect_url)

        return self.get_response(request)