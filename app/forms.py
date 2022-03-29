from django import forms
from .models import Post,comment
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class postform(forms.ModelForm):
	author = Post.author
	class Meta:
		model = Post
		fields = ['title','author','img','detail']

		
class Registration(UserCreationForm):
	email = forms.EmailField()
	class Meta:
		model = User
		fields = ['username','email','password1','password2']

	def __init__(self,*args,**kwargs):
		super(Registration,self).__init__(*args,**kwargs)

		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['password1'].widget.attrs['class'] = 'forms-control'
		self.fields['password2'].widget.attrs['class'] = 'form-control'

class commentForm(forms.ModelForm):
	class Meta:
		model = comment
		fields = ['name','body']
		def __init__(self,*args,**kwargs):
			super(Registration,self).__init__(*args,**kwargs)

			self.fields['name'].widget.attrs['class'] = 'form-control'

class profileupdate(UserCreationForm):
	email = forms.EmailField()
	class Meta:
		model = User
		fields = ['username','email','password1']

	def __init__(self,*args,**kwargs):
		super(profileupdate,self).__init__(*args,**kwargs)

		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['password1'].widget.attrs['class'] = 'forms-control'
