from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    author = models.CharField(null=True, max_length=20)
    is_bestselling = models.BooleanField(default=False)
    slug = models.SlugField(default="",null=False, db_index=True, blank=True)

    '''
    now django will create an table named, book in the database and it 
    will also initialize the two columns named title and rating
    and the id column will be automatically initiated by the django 
    and also it will the auto increment column.
    '''
    # overriding the str dunder method from the model class
    def __str__(self):
        return f"Book name is {self.title} and it's rating is {self.rating}"
    
    #overriding the absolute ulr function of the model class
    def get_absolute_url(self):
        return reverse("books_details", args=[self.slug])
    
    def save(self,*args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)