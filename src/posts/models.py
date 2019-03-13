from tinymce import HTMLField
from django.db import models
from django.contrib.auth import get_user_model
from slugger import AutoSlugField
from django.urls import reverse
# Create your models here.
User = get_user_model()


def upload_location(instance, filename):
    return "%s/%s" %(instance.slug, filename)


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.username

class Category(models.Model):
    title = models.CharField(max_length=20)
    slug = AutoSlugField(populate_from='title')
    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length = 100)
    slug = AutoSlugField(populate_from='title')
    overview = models.CharField(max_length= 200)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = HTMLField()
    comment_count = models.IntegerField(default=0)
    view_count = models.IntegerField(default=0)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    thumbnail = models.ImageField(
        upload_to=upload_location,
        null=True, 
        blank=True)
    category = models.ManyToManyField(Category)
    featured = models.BooleanField()
    previous_post = models.ForeignKey('self', related_name= 'previous', on_delete=models.SET_NULL, blank=True, null=True)
    next_post = models.ForeignKey('self', related_name= 'next', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.title