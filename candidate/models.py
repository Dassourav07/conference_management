from django.db import models
from django.contrib.auth.models import User

class Candidate(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic= models.ImageField(upload_to='profile_pic/Candidate/',null=True,blank=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=False)
    pdf = models.FileField(upload_to='paper/Candidate/', null=True,blank=True)
   
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_instance(self):
        return self
    def __str__(self):
        return self.user.first_name
 
class pdf(models.Model):
    pdf = models.FileField(upload_to='paper/Cndidate/')

    def __str__(self):
            return self.name


 
 