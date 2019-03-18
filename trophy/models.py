from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Projects(models.Model):

    projo_pic = models.ImageField(upload_to='projo-pic/')
    title = models.CharField(max_length=50)
    link = models.URLField(max_length=250)
    user = models.ForeignKey(User,null=True)

class Profile(models.Model):

    profile_pic = models.ImageField(upload_to='profile-pic/')
    bio = models.TextField()
    phone_number = models.IntegerField()

class Rating(model.Model):
    design = models.IntegerField()
    usability = models.IntegerField()
    content = models.IntegerField()
    




