from django.db import models
from django.contrib.auth.models import User

from django.utils import timezone
from django.urls import reverse
from PIL import Image
from ckeditor.fields import RichTextField

class Post(models.Model):
	title = models.CharField(max_length = 100)
	img = models.ImageField( default = 'default.jpg',upload_to = 'Images')
	author = models.ForeignKey(User, on_delete = models.CASCADE)
	detail = RichTextField(blank=True, null=True)
	created = models.DateTimeField(default = timezone.now)
	likes = models.ManyToManyField(User,related_name='blog')

	def __str__(self):
		return str(self.title)

	def total_likes(self):
		return str(self.likes.count())

	def get_absolute_url(self):
		#return reverse('show-one', args = (str(self.id)) )
		return reverse('show-post')

class comment(models.Model):
	post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
	name = models.CharField(max_length=255)
	body = RichTextField()
	date= models.DateTimeField(default = timezone.now)

	def __str__(self):
		return str(self.body[:50])




