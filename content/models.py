from django.db import models


class BlockType(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Content(models.Model):
    block = models.ForeignKey(BlockType, on_delete=models.CASCADE)


class Block(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    img = models.ImageField(upload_to='media/content')

    def __str__(self):
        return self.title

    # class Meta:
    #     abstract = True

