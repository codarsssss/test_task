from django.db import models


class ModelA(models.Model):
    a_one = models.CharField(max_length=255, blank=True)
    a_two = models.CharField(max_length=255, blank=True)
    a_three = models.CharField(max_length=255, blank=True)

    # def __str__(self):
    #     return self.__class__.__name__


class ModelB(models.Model):
    b_one = models.CharField(max_length=255, blank=True)
    b_two = models.CharField(max_length=255, blank=True)
    b_three = models.CharField(max_length=255, blank=True)


class ModelC(models.Model):
    c_one = models.CharField(max_length=255, blank=True)
    c_two = models.CharField(max_length=255, blank=True)
    c_three = models.CharField(max_length=255, blank=True)


class MyModels(models.Model):
    name = models.CharField(max_length=100, blank=True)
