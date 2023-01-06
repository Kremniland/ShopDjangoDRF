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

    # def email_field(self):
    #     '''При обращении к email_field вернет email User'''
    #     return User.objects.get(pk=self.user.pk).email

    def __str__(self):
        return f'{self.user}'

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
        ordering = ['user']


class ContactModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    message = models.CharField(max_length=5000)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} - {self.email}'

    class Meta:
        verbose_name = 'Обратная связь'
        verbose_name_plural = 'Обратная связь'
        ordering = ['create_date']

