from django.db import models

# Create your models here.

POSITION_LEVEL_CHOICE = (('t1','T1'),('t2','T2'),('t3','T3'),('t4','T4'),('m1','M1'),('m2','M2'),('m3','M3'),
                         ('m4','M4'),('s1','S1'),('s2','S2'),('l1','L1'),('l2','L2'))

class Position(models.Model):
    position_name = models.CharField(max_length=50)
    level = models.CharField(choices=POSITION_LEVEL_CHOICE , max_length=50)

    def __str__(self):
        return self.position_name

class BankNames(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class IdentityChoice(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Language(models.Model):
    code = models.CharField(max_length=2)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
