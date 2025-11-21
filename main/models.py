from django.conf import settings
from django.db import models
from django.template.defaultfilters import slugify


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Post(models.Model):

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, blank=True, null=True, verbose_name='Автор')
    title = models.CharField(max_length=50, verbose_name="Заголовок")
    slug = models.SlugField(unique=True, verbose_name="Слаг")
    text_content = models.TextField(verbose_name='Содержание статьи')
    is_published = models.BooleanField(default=True, verbose_name="Опубликовать")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    image = models.ImageField(blank=True, null=True, verbose_name="Изображение")
    categories = models.ManyToManyField(Category, blank=True, related_name='posts', verbose_name="Категория")

    def save(self, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(**kwargs)

    def categories_list(self):
        return ", ".join(c.name for c in self.categories.all())



