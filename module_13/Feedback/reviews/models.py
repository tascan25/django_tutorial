from django.db import models

# Create your models here.
class Reviews(models.Model):
    user_name = models.CharField(max_length=100)
    review_text = models.TextField()
    rating = models.IntegerField()
    
    #overriding the str dunder method the mdoels class
    def __str__(self):
        return f" username: {self.user_name}, review_text: {self.review_text}, rating: {self.rating}"