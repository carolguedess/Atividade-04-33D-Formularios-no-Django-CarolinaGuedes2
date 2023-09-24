from django.db import models

# Create your models here.
class sucessos(models.Model):
  title=models.CharField(max_length=50)
  peças=models.CharField(max_length=50)
  evoluçao=models.CharField(max_length=50)
  estampas=models.CharField(max_length=60)
  gênero=models.CharField(max_length=50)

class transformacao(models.Model):
  OPTIONS=[
    ("B",'before 90'),
    ("W", 'while 90'),
    ("A", 'after 90'),
  ]
  title=models.CharField(max_length=50)
  frequencia=models.CharField(max_length=50)
  over_the_years=models.CharField(max_length=1,choices=OPTIONS)
  ordem=models.IntegerField()