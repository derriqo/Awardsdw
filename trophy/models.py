from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Project(models.Model):

    projo_pic = models.ImageField(upload_to='projo-pic/')
    title = models.CharField(max_length=50)
    link = models.URLField(max_length=250)
    user = models.ForeignKey(User,null=True)

    def __str__(self):
        return self.title

    def save_project(self):
        self.save()
    
    def delete_project(self):
        self.objects.get(id=self.id).delete()

    @classmethod
    def search_by_projectname(cls,idea):
        projects = cls.objects.filter(title__icontains=idea)
        return projects

class Profile(models.Model):

    profile_pic = models.ImageField(upload_to='profile-pic/',default='default.jpg')
    bio = models.TextField()
    phone_number = models.IntegerField()
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile',null=True)

    def __str__(self):
        return self.user.username
    
    def save_profile(self):
        self.save()
    
    @classmethod
    def delete_profile(cls,derrick):
        cls.delete(derrick)
    


class Rating(models.Model):

    design = models.IntegerField(default=0)
    usability = models.IntegerField(default=0)
    content = models.IntegerField(default=0)
    project = models.ForeignKey(Project,on_delete=models.CASCADE,null=True)
    profile = models.ForeignKey(Profile,related_name='rating',null=True)
    comment = models.CharField(max_length=50,null=True)

    def __str__(self):
        return self.profile



