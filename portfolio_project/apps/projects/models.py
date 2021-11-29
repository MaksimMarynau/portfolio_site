from django.db import models


from additions.models import Tool


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    tool_used = models.ManyToManyField(Tool, related_name='tools')
    image = models.ImageField(
        upload_to='projects/',
        blank=True,
        default='projects/no-image.jpg'
    )


class ProjectImages(models.Model):
    project = models.ForeignKey(Project, default=None, on_delete=models.CASCADE)
    images = models.ImageField(
        upload_to='projects/additional/',
        blank=True,
        default='projects/additional/no-image.jpg'
    )

    def __str__(self):
        return self.project.title
