from django.db import models
from django.contrib.auth.models import User

# Create your models here.

def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.id, filename)

class Graph(models.Model):
    user = models.ForeignKey(to=User, null=True, on_delete=models.SET_NULL)
    title = models.CharField('Название', max_length=50)
    graph = models.FileField('График', blank=True, upload_to=user_directory_path)

    def __str__(self):
        return self.title