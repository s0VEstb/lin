from django.db import models

class Books(models.Model):
    GENRE_CHOICE = (
        ('Фантастика', 'Фантастика'),
        ('Романтика', 'Романтика'),
        ('Научный', 'Научный')
    )
    image = models.ImageField(upload_to='book/', verbose_name='Загрузите картинку')
    title = models.CharField(max_length=100, verbose_name='Укажите название книги')
    description = models.TextField(verbose_name='Укажите описание к книге')
    price = models.FloatField(verbose_name='Укажите цену')
    start_book = models.DateField(verbose_name='Укажите дату выхода')
    genre = models.CharField(max_length=100, choices=GENRE_CHOICE, default='Фантастика',
                             verbose_name='Укажите жанр')
    email = models.EmailField(verbose_name='Укажите почту автора')
    author = models.CharField(max_length=30, verbose_name='Укажите имя автора')
    link = models.URLField(verbose_name='Укажите ссылку', null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'книга'
        verbose_name_plural = 'книги'

    def __str__(self):
        return f'{self.title}-{self.price}$'