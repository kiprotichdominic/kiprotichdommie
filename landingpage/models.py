from django.db import models
from PIL import Image

# Create your models here.


class PortfolioProject(models.Model):
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=300)
    link = models.URLField(max_length=200)
    project_image = models.ImageField(upload_to='Portfolio_projects')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Portfolio Project'
        verbose_name_plural = 'Portfolio Project'

    def save(self, *args, **kwargs):
        super(PortfolioProject, self).save(*args, **kwargs)

        img = Image.open(self.project_image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.project_image.path)
