from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
import pytz


TIMEZONES = tuple(zip(pytz.all_timezones, pytz.all_timezones))
TYPE_CHOICES = (
    ('primary', 'Первичный'),
    ('repeated', 'Повторный'),
    ('external', 'Внешний'),
    ('indirect', 'Косвенный'),
)
SEX_CHOICES = {
    ('male', 'Мужской'),
    ('female', 'Женский'),
    ('unknown', 'Неизвестно'),
}


class User(AbstractUser):
    identity_number = models.CharField(
        max_length=220, null=True, blank=True, verbose_name="Идентификационный номер"
    )
    mobile_phone = PhoneNumberField(
        max_length=20, null=False, blank=False, unique=True, verbose_name="Номер телефона"
    )
    last_name = models.CharField(
        max_length=150, null=True, blank=True, verbose_name="Фамилия"
    )
    first_name = models.CharField(
        max_length=150, null=True, blank=True, verbose_name="Имя"
    )
    middle_name = models.CharField(
        max_length=150, null=True, blank=True, verbose_name="Отчество"
    )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='Дата создания'
    )
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name='Дата изменения'
    )
    status_updated = models.DateTimeField(
        verbose_name='Дата изменения статуса'
    )
    is_active = models.BooleanField(
        default=True, verbose_name='Статус'
    )
    client_type = models.CharField(
        max_length=150, choices=TYPE_CHOICES, null=True, blank=True, verbose_name="Тип"
    )
    sex = models.CharField(
        max_length=150, choices=TYPE_CHOICES, null=True, blank=True, verbose_name="Пол"
    )
    timezone = models.CharField(
        max_length=32, choices=TIMEZONES, default='UTC'
    )


class AdditionalNumbers(models.Model):
    user = models.ForeignKey(
        "auth.User", on_delete=models.CASCADE, verbose_name="user", related_name="additional_numbers",
    )
    number = PhoneNumberField(
        max_length=20, null=False, blank=False, verbose_name="Дополнительные номера"
    )


class Email(models.Model):
    user = models.ForeignKey(
        "auth.User", on_delete=models.CASCADE, verbose_name="user", related_name="emails",
    )
    models.EmailField(
        blank=True, null=True, verbose_name="Почта"
    )


class SocialMedias(models.Model):
    user = models.ForeignKey(
        "auth.User", on_delete=models.CASCADE, verbose_name="user", related_name="social_medias",
    )
    ok = models.CharField(
        max_length=220, null=True, blank=True, verbose_name="Одноклассники"
    )
    instagram = models.CharField(
        max_length=220, null=True, blank=True, verbose_name="Инстаграм"
    )
    telegram = models.CharField(
        max_length=220, null=True, blank=True, verbose_name="Телеграм"
    )
    whatsapp = models.CharField(
        max_length=220, null=True, blank=True, verbose_name="Вотсап"
    )
    viber = models.CharField(
        max_length=220, null=True, blank=True, verbose_name="Вайбер"
    )


class VkAccounts(models.Model):
    social_medias = models.ForeignKey(
        "auth.SocialMedias", on_delete=models.CASCADE, verbose_name="social_medias", related_name="vk_accounts",
    )
    account = models.CharField(
        max_length=220, null=True, blank=True, verbose_name="Вк"
    )


class FbAccounts(models.Model):
    social_medias = models.ForeignKey(
        "auth.SocialMedias", on_delete=models.CASCADE, verbose_name="social_medias", related_name="fb_accounts",
    )
    account = models.CharField(
        max_length=220, null=True, blank=True, verbose_name="Фб"
    )
