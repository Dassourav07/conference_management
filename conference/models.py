from threading import active_count
from django.db import models
from candidate.models import Candidate
 

 
class Category(models.Model):
    category_name =models.CharField(max_length=200)
    creation_date =models.DateField(auto_now=True)
    def __str__(self):
        return self.category_name

class Conference(models.Model):
    category= models.ForeignKey('Category', on_delete=models.CASCADE)
    conference_name=models.CharField(max_length=200)
    Duration=models.PositiveIntegerField()
    venue=models.CharField(max_length=200)
    Date= models.DateTimeField(auto_now_add=False,auto_now=False,blank=True)
    creation_date =models.DateField(auto_now=True)
    pdf = models.FileField(upload_to='paper/Candidate/', null=True,blank=True)
   
    def __str__(self):
        return self.conference_name
 
class ConferenceRecord(models.Model):
    candidate= models.ForeignKey(Candidate, on_delete=models.CASCADE)
    conference= models.ForeignKey(Conference, on_delete=models.CASCADE)
    status = models.CharField(max_length=100,default='Pending')
    creation_date =models.DateField(auto_now=True)
    def __str__(self):
        return self.conference

class Question(models.Model):
    candidate= models.ForeignKey(Candidate, on_delete=models.CASCADE)
    description =models.CharField(max_length=500)
    admin_comment=models.CharField(max_length=200,default='Nothing')
    asked_date =models.DateField(auto_now=True)
    def __str__(self):
        return self.description