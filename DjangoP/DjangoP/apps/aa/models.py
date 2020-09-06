from django.db import models
from django.utils import timezone
import datetime
class Arti(models.Model):
    arti_title = models.CharField('Название', max_length=200)
    arti_text = models.TextField('техт')
    pub_date = models.DateTimeField('дата')
    def __str__(self):
        return self.arti_title

    def was_publ_res(self):
        return self.pub_date >=(timezone.now() - datetime.timedelta(days=7))
    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"

class Comm(models.Model):
    arti = models.ForeignKey(Arti, on_delete=models.CASCADE)
    author_name = models.CharField('имя', max_length=50)
    comment_text = models.CharField('', max_length=200)
    def __str__(self):
        return self.author_name
    class Meta:
        verbose_name = "Комент"
        verbose_name_plural = "Коменты"