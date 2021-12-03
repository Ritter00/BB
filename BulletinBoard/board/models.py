from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Category(models.Model):
    name = models.CharField('Категория', max_length=64, unique=True)

    def __str__(self):
        return f'{self.name}'


class Poster(models.Model):
    date_creation = models.DateTimeField("Дата публикации", auto_now_add= True)
    date_upgrade = models.DateTimeField("Последнее обновление", auto_now= True)
    category = models.ForeignKey(Category, on_delete= models.CASCADE)
    author = models.ForeignKey(User, on_delete= models.CASCADE, blank=True)
    title = models.CharField("Заголовок", max_length=128)
    content = RichTextUploadingField("Контент", blank=True)

    def __str__(self):
        return f'{self.title}'


class ResponseTTPoster(models.Model):
    date_creation = models.DateTimeField("Дата комментария", auto_now_add= True)
    author = models.ForeignKey(User, on_delete= models.CASCADE, blank=True)
    commentPoster = models.ForeignKey(Poster, on_delete= models.CASCADE)
    text = models.TextField('Текст сообщения')

    def __str__(self):
        return f'{self.text[:128]}'

