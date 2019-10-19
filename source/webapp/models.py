from django.db import models

class Poll(models.Model):

    question = models.TextField(max_length = 200, null = False, blank = False, verbose_name = 'Вопрос')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Время изменения')

class Choice(models.Model):

    text = models.TextField(max_length=200,null=False,blank=False,verbose_name='Ответ')
    poll = models.ForeignKey('Poll',on_delete=models.CASCADE, null=True, blank=True, verbose_name='Вопрос',
                                 related_name='choice_poll')


# Create your models here.
