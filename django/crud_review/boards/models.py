from django.db import models
from imagekit.models import ProcessedImageField, ImageSpecField
from imagekit.processors import Thumbnail

def board_image_path(instance,filename):
    return f'boards/{instance.pk}번글/images/{filename}'

class Board(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    #image = models.ImageField(blank=True)
    image = ProcessedImageField(
        upload_to=board_image_path,
        processors=[Thumbnail(200,300)],
        format='jpeg',
        options={'quality':90},
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)

    def __str__(self):
        return f'<Board{self.board_id}: Comment({self.id} - {self.content})>'