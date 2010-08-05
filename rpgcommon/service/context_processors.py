from django.conf import settings

def service_tokens(request):
    return {
        'facebook_application_id': getattr(settings, 'FACEBOOK_APPLICATION_ID', ''),
        'google_analytics_code' : getattr(settings, 'GOOGLE_ANALYTICS_CODE', ''),
    }
