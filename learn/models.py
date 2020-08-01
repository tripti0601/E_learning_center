from django.db import models
from django.urls import reverse

class Question_Model(models.Model):
    video = models.FileField(upload_to='videos/')
    publication = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    std = models.IntegerField()
    unit_name = models.CharField(max_length=200)
    exercise = models.IntegerField(null=True)
    Question_no = models.IntegerField()
    Question = models.CharField(max_length=500)
    like = models.IntegerField(default=0)

    def __str__(self):
    	return self.Question

    def get_video_url(self):
    	return reverse("detail-view",kwargs={'question_id':self.id})

    def get_question_url(self):
    	return reverse("liked",kwargs={'question_id':self.id})




# Create your models here.
