from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.db.models import Q

UserModel = get_user_model()


# classe pra permitir o login apartir do email cadastrado.
# nao sei como funciona.
# - Gustavo


class CustomEmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = UserModel.objects.get(
                Q(email__iexact=username)
                | Q(email__iexact=username + "@fiocruz.br")
                | Q(email__iexact=username + "@into.saude.gov.br")
            )
        except UserModel.DoesNotExist:
            UserModel().set_password(password)
            return
        except UserModel.MultipleObjectsReturned:
            user = (
                UserModel.objects.filter(
                    Q(username__iexact=username) | Q(email__iexact=username)
                )
                .order_by("id")
                .first()
            )

        if user.check_password(password) and self.user_can_authenticate(user):
            return user
