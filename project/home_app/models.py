from django.db import models


class ModelA(models.Model):
    a_one = models.CharField(max_length=255, blank=True)
    a_two = models.CharField(max_length=255, blank=True)
    a_three = models.CharField(max_length=255, blank=True)


class ModelB(models.Model):
    b_one = models.CharField(max_length=255, blank=True)
    b_two = models.CharField(max_length=255, blank=True)
    b_three = models.CharField(max_length=255, blank=True)


class ModelC(models.Model):
    c_one = models.CharField(max_length=255, blank=True)
    c_two = models.CharField(max_length=255, blank=True)
    c_three = models.CharField(max_length=255, blank=True)
