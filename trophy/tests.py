from django.test import TestCase
from .models import Profile,Project
from django.contrib.auth.models import User

# Create your tests here.
class ProfileTestClass(TestCase):
    
    # Set up method
    def setUp(self):
        self.user=User(username='derrick',email='derrick@gmail.com',password='qwerty123')
        self.user.save()
        self.derrick= Profile(profile_pic ='derrick.jpg',bio='junior developer',phone_number='07123453',user=self.user)
        self.derrick.save_profile()

    #Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.derrick, Profile))
    
    #Testing Save Method
    def test_save_method(self):
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles)>0)
    
    #Testing for Delete
    def test_delete_method(self):
        fetch_profile = Profile.objects.filter(user__username='derrick').first()
        Profile.delete_profile(fetch_profile)
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) == 0)