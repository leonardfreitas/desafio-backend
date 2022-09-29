from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager, PermissionsMixin
from django.contrib.auth.validators import UnicodeUsernameValidator


class User(AbstractBaseUser, PermissionsMixin):

    class AccessLevel(models.TextChoices):
        ADMIN = 'ADMIN', 'Administrador'
        PLAYER = 'PLAYER', 'Jogador'

    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        max_length=30,
        unique=True,
        help_text='Obrigatório. Máximo 30 caracteres. Letras, dígitos e @/./+/-/_ apenas.',
        validators=[username_validator],
        error_messages={
            'unique': "Esse nome de usuário já está em uso",
        },
    )
    email = models.EmailField(null=True, blank=True, unique=True)
    access_level = models.CharField(max_length=20, choices=AccessLevel.choices, default=AccessLevel.PLAYER)
    photo = models.URLField(max_length=255, null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    # timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'

    REQUIRED_FIELDS = ['access_level', 'email']

    class Meta:
        verbose_name = 'usuário'
        verbose_name_plural = 'usuários'
        ordering = ['-created_at']

    def __str__(self):
        return self.username
