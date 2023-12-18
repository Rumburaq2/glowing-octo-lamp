from allauth.socialaccount.signals import pre_social_login
from allauth.socialaccount.models import SocialAccount
from django.dispatch import receiver
from django.core.exceptions import PermissionDenied

@receiver(pre_social_login)
def restrict_by_email_domain(sender, request, sociallogin, **kwargs):
    email_domain = 'student.gyarab.cz'
    email = sociallogin.account.extra_data.get('email', '')

    if not email.endswith('@' + email_domain):
        # If the email does not end with '@gyarab.cz', deny access
        raise PermissionDenied('Access denied. Only @gyarab.cz emails are allowed.')