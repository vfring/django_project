from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from PIL import Image


class GroupCreation(models.Model):  # add Location Field (will need to sort by) and add to forms field
    group_name = models.CharField(max_length=120)
    group_desc = models.TextField()
    img_group = models.ImageField(default='default.jpg', upload_to='group_pics')
    date_posted = models.DateTimeField(default=timezone.now)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.group_name

    def save(self, *args, **kwargs):
        super(GroupCreation, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
