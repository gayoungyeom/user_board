from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50) # 제목
    description = models.TextField() # 본문
    pub_date = models.DateTimeField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.description[:150]