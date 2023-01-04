from django.db import models
from django.contrib.auth.models import User


class Client(models.Model):
    '''Модель клиента'''
    BENEFIT = ( # Льгота на тариф
        ('full', 'Full'),
        ('student', 'Student'),
        ('pensioner', 'Pensioner')
    )
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    discount_type = models.CharField(choices=BENEFIT, max_length=10)
    address = models.CharField(max_length=150)

    # def __str__(self):
    #     '''Вернет user + email'''
    #     email = User.objects.get(pk=self.user.pk).email
    #     return f'{self.user} - {email}'

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
        ordering = ['user']


