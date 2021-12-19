from django.contrib.auth.models import AbstractUser
from django.db import models
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel
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


class Client(AbstractUser):
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
        null=True, blank=True, verbose_name='Дата изменения статуса'
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
        null=True, blank=True, max_length=32, choices=TIMEZONES, default='UTC'
    )
    departments = models.ManyToManyField(
        'Department', through='ClientInDep', through_fields=('client', 'department'),
        verbose_name='Департаменты', related_name='clients'
    )

    def save(self, *args, **kwargs):
        if self.identity_number != '':
            self.identity_number += '01'
        super().save(*args, **kwargs)


class AdditionalNumbers(models.Model):
    user = models.ForeignKey(
        "Client", on_delete=models.CASCADE, verbose_name="user", related_name="additional_numbers",
    )
    number = PhoneNumberField(
        max_length=20, null=False, blank=False, verbose_name="Дополнительные номера"
    )


class Email(models.Model):
    user = models.ForeignKey(
        "Client", on_delete=models.CASCADE, verbose_name="user", related_name="emails",
    )
    models.EmailField(
        blank=True, null=True, verbose_name="Почта"
    )


class SocialMedias(models.Model):
    user = models.ForeignKey(
        "Client", on_delete=models.CASCADE, verbose_name="user", related_name="social_medias",
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
        "SocialMedias", on_delete=models.CASCADE, verbose_name="social_medias", related_name="vk_accounts",
    )
    account = models.CharField(
        max_length=220, null=True, blank=True, verbose_name="Вк"
    )


class FbAccounts(models.Model):
    social_medias = models.ForeignKey(
        "SocialMedias", on_delete=models.CASCADE, verbose_name="social_medias", related_name="fb_accounts",
    )
    account = models.CharField(
        max_length=220, null=True, blank=True, verbose_name="Фб"
    )


class LegalEntity(models.Model):
    identity_number = models.CharField(
        max_length=220, null=True, blank=True, verbose_name="Идентификационный номер"
    )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='Дата создания'
    )
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name='Дата изменения'
    )
    full_name = models.CharField(
        max_length=150, null=True, blank=True, verbose_name="Полное название"
    )
    short_name = models.CharField(
        max_length=150, null=True, blank=True, verbose_name="Сокращенное название"
    )
    inn = models.CharField(
        max_length=220, null=True, blank=True, verbose_name="ИНН"
    )
    kpp = models.CharField(
        max_length=220, null=True, blank=True, verbose_name="КПП"
    )
    departments = models.ManyToManyField(
        'Department', verbose_name='Департаменты', related_name='legalentities'
    )

    def save(self, *args, **kwargs):
        if self.identity_number != '':
            self.identity_number += '02'
        super().save(*args, **kwargs)


class Department(MPTTModel):
    identity_number = models.CharField(
        max_length=220, null=True, blank=True, verbose_name="Идентификационный номер"
    )

    name = models.CharField(max_length=255, null=False, blank=False, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.identity_number != '':
            self.identity_number += '03'
        if self.parent.level == 7:
            raise ValueError(u'Достигнута максимальная вложенность!')
        super().save(*args, **kwargs)

    class MPTTMeta:
        order_insertion_by = ['name']


class ClientInDep(models.Model):
    client = models.ForeignKey(
        Client, on_delete=models.CASCADE, verbose_name='Клиент'
    )
    department = models.ForeignKey(
        Department, on_delete=models.CASCADE, verbose_name='Департамент'
    )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='Дата добавления в департамент'
    )
