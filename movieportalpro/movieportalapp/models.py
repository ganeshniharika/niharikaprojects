from django.db import models

class Telugu(models.Model):
    m_name=models.CharField(max_length=100)
    m_director=models.CharField(max_length=100)
    m_hero=models.CharField(max_length=100)
    m_heroine=models.CharField(max_length=100)

class Hindi(models.Model):
    m_name = models.CharField(max_length=100)
    m_director = models.CharField(max_length=100)
    m_hero = models.CharField(max_length=100)
    m_heroine = models.CharField(max_length=100)

class English(models.Model):
    m_name = models.CharField(max_length=100)
    m_director = models.CharField(max_length=100)
    m_hero = models.CharField(max_length=100)
    m_heroine = models.CharField(max_length=100)
class Bookdata(models.Model):
    m_id=models.IntegerField()
    m_name=models.CharField(max_length=100)
    m_time=models.CharField(max_length=20)
    m_theatre=models.CharField(max_length=100)
    c_class=models.CharField(max_length=100)
