from django.db import models


class Block(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    img = models.ImageField(upload_to='media/content', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        abstract = True


class BlockTitle(Block):
    point = models.ManyToManyField('BlockTitleItem')

    class Meta:
        verbose_name = 'Главный блок'
        verbose_name_plural = 'Главные блоки'


class BlockReviews(Block):
    point = models.ManyToManyField('BlockReviewItem')

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'


class BlockSkill(Block):
    icon_class = models.ForeignKey('IconStyle', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Свойство'
        verbose_name_plural = 'Свойства'


class BlockAbout(Block):
    point = models.ManyToManyField('BlockAboutItem')

    class Meta:
        verbose_name = 'О продукте'
        verbose_name_plural = 'О продукте'


class IconStyle(models.Model):
    icon_class = models.CharField(max_length=40)

    class Meta:
        verbose_name = 'Класс иконки'
        verbose_name_plural = 'Класс иконок'

    def __str__(self):
        return self.icon_class


class BlockAboutItem(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Пункт блока "О продукте"'
        verbose_name_plural = 'Пункты блока "О продукте"'

    def __str__(self):
        return self.name


class BlockTitleItem(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Пункт блока "Главный блок"'
        verbose_name_plural = 'Пункты блока "Главный блок"'

    def __str__(self):
        return self.name


class BlockReviewItem(models.Model):
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    img = models.ImageField(upload_to='media/reviewItem')
    text = models.TextField(max_length=400)

    class Meta:
        verbose_name = 'Пункт отзыва'
        verbose_name_plural = 'Пункты отзывов'

    def __str__(self):
        return self.name


class Message(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name