from django.db import models

class Article(models.Model):
    title = models.CharFild(max_length=60,default="title")
    content = models.TextField(null=True)