from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class User(models.Model):
  username: models.CharField(max_length=50)

class category(models.Model):
  name = models.CharField(max_length=30)

class Post(models.Model):

  name = models.CharField(max_length =60)
  content = models.TextField()
  #image = CloudinaryField('image')
  category = models.OneToOneField(category, on_delete=models.CASCADE)
  user= models.ForeignKey(User,on_delete=models.CASCADE)
  #votes = models.ManyToManyField(votes)
  date_posted = models.DateTimeField(auto_now_add=True)



