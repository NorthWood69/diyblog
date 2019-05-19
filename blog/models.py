from django.db import models
from datetime import date
from django.urls import reverse
from django.contrib.auth.models import User

class Blogger(models.Model):
    name = models.ForeignKey(User, verbose_name='Name', on_delete=models.SET_NULL, null=True, help_text='')
    bio = models.TextField('Bio', max_length=1000, help_text='')

    class Meta:
        ordering = ["name","bio"]

    def get_absolute_url(self):
        return reverse('blogs-by-blogger', args=[str(self.id)])

    def __str__(self):
        return self.name.username

class Blog(models.Model):
    title = models.CharField(max_length=100, help_text='')
    post_date = models.DateField('Post date', default=date.today, help_text='')
    author = models.ForeignKey('Blogger', verbose_name='Author', on_delete=models.SET_NULL, null=True, help_text='')
    description = models.TextField('Description', max_length=1000, help_text='')

    class Meta:
        ordering = ['-post_date']

    def get_absolute_url(self):
        return reverse('blog-detail', args=[str(self.id)])

    def __str__(self):
        return self.title

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, help_text='')
    comment_date = models.DateTimeField('Created', auto_now_add=True, help_text='')
    comment = models.TextField('Comment', max_length=1000, help_text='')
    blog= models.ForeignKey(Blog, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-comment_date']

    def __str__(self):
        if len(self.comment) > 75:
            string = self.comment[:72] + '...'
        else:
            string = self.comment
        return string
