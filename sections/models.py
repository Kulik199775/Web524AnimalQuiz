from django.db import models
from django.utils.translation import gettext_lazy as _

from users.models import NULLABLE


class Section(models.Model):
    title = models.CharField(verbose_name=_('Title'), max_length=150, unique=True)
    description = models.TextField(verbose_name=_('Description'), **NULLABLE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Section')
        verbose_name_plural = _('Sections')
        ordering = ['id']


class Content(models.Model):
    section = models.ForeignKey(Section, verbose_name=_('Section'), on_delete=models.CASCADE)
    title = models.CharField(verbose_name=_('Title'), max_length=150, unique=True)
    content = models.TextField(verbose_name=_('Content'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Content')
        verbose_name_plural = _('Content')
        ordering = ['id']
