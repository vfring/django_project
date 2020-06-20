from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# make it so candidates get to this by clicking on location ("run") selection
# election picker,

class CandidateProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pimage = models.ImageField(default='default.jpg', upload_to='cand_pics')
    fir_name = models.CharField(max_length=100)
    las_name = models.CharField(max_length=100)
    run_party = models.CharField(max_length=240)
    cand_plat = models.TextField()

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super(CandidateProfile, self).save(*args, **kwargs)

        img = Image.open(self.pimage.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.pimage.path)
