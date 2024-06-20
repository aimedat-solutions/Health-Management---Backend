from django.contrib.auth.backends import BaseBackend
from django.db.models import Q
from .models import CustomUser

class PhoneNumberOrEmailBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = CustomUser.objects.get(
                Q(phone_number=username) | Q(email=username)
            )
            if user.check_password(password):
                return user
        except CustomUser.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return CustomUser.objects.get(pk=user_id)
        except CustomUser.DoesNotExist:
            return None