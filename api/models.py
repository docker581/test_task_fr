from django.db import models


class Poll(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name='Название опроса',
    )
    description = models.TextField(verbose_name='Описание')
    date_start = models.DateField(
        auto_now_add=True,
        editable=False,
        verbose_name='Дата начала',
    )
    date_end = models.DateField(verbose_name='Дата окончания')
    session_id = models.CharField(
        max_length=100,
        blank=True,
        verbose_name='ID сессии',
    )

    class Meta:
        verbose_name = 'Опрос'
        verbose_name_plural = 'Опросы'

    def __str__(self):
        return self.name


class Question(models.Model):
    TYPES = (
        ('текст', 'Ответ текстом'),
        ('один вариант', 'Один вариант ответа'),
        ('несколько вариантов', 'Несколько вариантов ответа'),
    )
    poll = models.ForeignKey(
        Poll,
        on_delete=models.CASCADE,
        related_name='questions',
        verbose_name='Опрос',
    )
    text = models.CharField(
        max_length=100,
        verbose_name='Текст вопроса',
    )
    type = models.TextField(
        max_length=100,
        choices=TYPES,
        verbose_name='Тип вопроса',
    )

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

    def __str__(self):
        return self.text    