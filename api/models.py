from django.db import models


class Poll(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name='Название опроса',
    )
    description = models.TextField(verbose_name='Описание')
    date_start = models.DateField(
        editable=False,
        verbose_name='Дата начала',
    )
    date_end = models.DateField(verbose_name='Дата окончания')
    slug = models.SlugField(
        unique=True,
        verbose_name='URL имя',
    )
    session_id = models.CharField(
        max_length=100,
        verbose_name='ID сессии',
    )

    class Meta:
        verbose_name = 'Опрос'
        verbose_name_plural = 'Опросы'

    def str(self):
        return self.name


class TypeChoices(models.TextChoices):
    TEXT = 'текст', 'text'
    OPTION = 'один вариант', 'one option'
    OPTIONS = 'несколько вариантов', 'several_options'


class Question(models.Model):
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
        choices=TypeChoices.choices,
        verbose_name='Тип вопроса',
    )

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

    def __str__(self):
        return self.text    