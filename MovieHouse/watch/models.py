from django.db import models
from movie.models import Movie
from series.models import Series
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Mwatchlist(models.Model):
    movie=models.ForeignKey(Movie,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)


    def __str__(self):
        return str(self.movie)

class Swatchlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    series = models.ForeignKey(Series, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.series)

class Freetrial(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    date1= models.DateField(default=timezone.now)
    exp_date = models.DateField(default=timezone.now)

    def __str__(self):
        return str(self.user)


class Freetriallist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)

class Month(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    amount=models.CharField(max_length=20)
    date1 = models.DateField(default=timezone.now)
    exp_date = models.DateField(default=timezone.now)

    def __str__(self):
        return str(self.user)

class Annual(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    amount=models.CharField(max_length=20)
    date1 = models.DateField(default=timezone.now)
    exp_date = models.DateField(default=timezone.now)
    def __str__(self):
        return str(self.user)

class Account(models.Model):
    acctnumber=models.IntegerField()
    acctype=models.CharField(max_length=50)
    balance=models.IntegerField()

    def __str__(self):
        return str(self.acctnumber)