from django.contrib.auth.models import AbstractUser
from django.db import models

from .managers import UserManager
from services.cpf import CPFLogics
from django.utils.translation import gettext_lazy as _

cpf = CPFLogics()


class UserModel(AbstractUser):
    username = None
    user_permissions = None
    first_name = None
    last_name = None
    groups = None

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]

    email = models.EmailField(max_length=100, unique=True, verbose_name=_("User Email"))
    name = models.CharField(max_length=100, verbose_name=_("User Name"))
    document = models.CharField(
        max_length=11,
        validators=[cpf.validate_cpf],
        verbose_name=_("User Document"),
        help_text=_("Just numbers"),
    )

    objects = UserManager()

    def __str__(self):
        return self.name

    class Meta:
        db_table = "user"
        verbose_name = _("User")
        verbose_name_plural = _("Users")
        managed = True
