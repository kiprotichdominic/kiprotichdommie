from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models
from PIL import Image


class CustomUser(AbstractUser):
    pass
    # add additional fields in here

    def __str__(self):
        return self.username


class Profile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    profile_image = models.ImageField(
        default='dommie.jpeg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.profile_image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.profile_image.path)
