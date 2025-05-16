from django.contrib import messages
from django.db import models, IntegrityError
from django.db.models import ProtectedError
from django_softdelete.models import SoftDeleteModel
from nath.settings import AUTH_USER_MODEL


class CustomBaseModel(SoftDeleteModel):
    created_at = models.DateTimeField(blank=True, auto_now_add=True)
    modified_at = models.DateTimeField(blank=True, auto_now=True)
    modified_by = models.ForeignKey(AUTH_USER_MODEL, blank=True, on_delete=models.CASCADE)

    class Meta:
        abstract = True

    def custom_discrete_save(self, request):
        try:
            self.modified_by = request.user
            obj = super().save()
            # retorna o objeto que foi salvo
            return obj

        except IntegrityError:
            # messages.warning(request, "Este registro já existe.")
            pass

        except Exception as e:
            # messages.warning(request, "Error na criação." + str(e))
            pass

    def custom_save(self, request, msg = None, *args, **kwargs):
        try:
            self.modified_by = request.user
            obj = super().save()
            if msg: 
                messages.success(request, msg)
            else:
                messages.success(request, "Cadastrado com sucesso.")
            # retorna o objeto que foi salvo
            return obj

        except IntegrityError:
            messages.warning(request, "Este registro já existe.")

        except Exception as e:
            messages.warning(request, "Error na criação." + str(e))

    def custom_update(self, request, msg=None):
        try:
            self.modified_by = request.user
            super().save()
            if msg: 
                messages.success(request, msg)
            else:
                messages.success(request, "Alterado com sucesso.")

        except IntegrityError:
            messages.warning(request, "Este registro já existe.")

        except Exception as e:
            messages.warning(request, "Error na alteração." + str(e))

    def custom_delete(self, request):
        try:
            self.modified_by = request.user
            super().save()
            super().delete()
            messages.success(request, "Excluido com sucesso.")
            return True

        except ProtectedError:
            messages.warning(request, "Este registro ainda está sendo usado em outro lugar.")

        except Exception as e:
            messages.warning(request, "Error ao excluir." + str(e))