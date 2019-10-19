from django.db import models

class Poll(models.Model):

    question = models.TextField(max_length = 200, null = False, blank = False, verbose_name = 'Вопрос')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Время изменения')

    def __str__(self):
        return self.question

class Choice(models.Model):

    text = models.TextField(max_length=400,null=False,blank=False,verbose_name='Ответ')
    poll = models.ForeignKey('Poll',on_delete=models.CASCADE, null=False, blank=False, verbose_name='Вопрос',
                                 related_name='choice_poll')
    def __str__(self):
        return  self.text

class Answer(models.Model):

    poll = models.ForeignKey('Poll',on_delete=models.PROTECT,null=False,blank=False,verbose_name='Вопрос',
                             related_name='answer_poll')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    choice = models.ForeignKey('Choice',on_delete=models.PROTECT,blank=False,null=False,verbose_name='ответ',
                               related_name='answer_choice')

# Create your models here.
