from django.db import models

# Create your models here.
class Scategory(models.Model):
    scname=models.CharField(max_length=50)
    simage=models.FileField(upload_to="image/simage",null=True,blank=True)

    def __str__(self):
        return self.scname

class Series(models.Model):
    sname=models.CharField(max_length=100)
    description=models.TextField()
    image=models.ImageField(upload_to="series/image",null=True,blank=True)
    video=models.FileField(upload_to="series/videos")
    language=models.CharField(max_length=100)
    rating_outof_10=models.IntegerField()
    season=models.IntegerField()
    no_of_episodes=models.IntegerField(default=5)
    category=models.ForeignKey(Scategory,on_delete=models.CASCADE,default=1)

    def __str__(self):
        return self.sname

class Episode(models.Model):
    esname=models.ForeignKey(Series,on_delete=models.CASCADE)
    episode_no=models.IntegerField()
    season=models.IntegerField()
    video=models.FileField(upload_to="videos",max_length=500)

    def __str__(self):
        return str(self.esname)