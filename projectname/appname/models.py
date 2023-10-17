from django.db import models

# Create your models here.
# models.py
from django.db import models

class GoogleSheetData(models.Model):
    Project_Executive = models.CharField(max_length=500 , default='')
    Name = models.CharField(max_length=300 , default='')
    Handle_Name = models.CharField(max_length=400 , default='')
    Password = models.CharField(max_length=100 , default='')
    Post_Url = models.CharField(max_length=500 , default='')
    Image_Type = models.CharField(max_length=200 , default='')
    Video_Type = models.CharField(max_length=200 , default='')
    Impressions = models.IntegerField(default='')
    Likes  = models.IntegerField(default='')
    Comments = models.IntegerField(default='')
    Retweet = models.IntegerField(default='')
    Followers  = models.IntegerField(default='0')
    Followings  = models.IntegerField(default='0')

    def __str__(self):
        return self.Name
    


