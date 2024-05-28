from django.db import models
from django.urls import reverse

from datetime import date

# Create your models here.

class Blogger(models.Model):
    """Model representing an author."""
    name = models.CharField(max_length=100)
    bio = models.TextField(
        max_length=1000, help_text="Enter a bio of the blogger")


    class Meta:
        ordering = ['name']

    def get_absolute_url(self):
        """Returns the URL to access a particular author instance."""
        return reverse('blogger-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return self.name
    

class Post(models.Model):
    title = models.CharField(max_length=100)
    post_date = models.DateField(auto_now_add =True)
    author = models.ForeignKey('Blogger', on_delete=models.CASCADE)    
    description = models.TextField(
        max_length=1000, help_text="Enter description of the post")
    
    class Meta:
        ordering = ['-post_date']

    def get_absolute_url(self):
        """Returns the URL to access a particular author instance."""
        return reverse('blog-detail', args=[str(self.id)])
    

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.title} ({self.author.name})'
    

class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE)   
    author = models.ForeignKey('Blogger', on_delete=models.CASCADE) 
    post_time = models.DateTimeField(auto_now_add =True)
    description = models.TextField(
        max_length=1000, help_text="Enter comment about blog")    
    
    class Meta:
        ordering = ['post_time']   
    
    def __str__(self):
        """String for representing the Model object."""
        return  f'{self.author.name} ({self.post_time})'
