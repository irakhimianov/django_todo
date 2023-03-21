from django.db import models
from django.contrib.auth import get_user_model

from core.models import BaseModel

User = get_user_model()


class Task(BaseModel):
    title = models.CharField('заголовок', max_length=120)
    description = models.TextField('описание', blank=True, default='')
    is_completed = models.BooleanField('выполнен', default=False)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'задача'
        verbose_name_plural = 'задачи'
        ordering = ('is_completed', '-created_at')

    def __str__(self):
        return self.title
