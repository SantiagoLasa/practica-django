# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Post(models.Model):
    titulo = models.CharField(max_length=50)
    texto = models.CharField(max_length=100)

    def __str__(self):
        return 'el post {}'.format(self.titulo)
