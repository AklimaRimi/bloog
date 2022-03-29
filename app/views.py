from django.shortcuts import render,redirect,get_object_or_404
from .models import Post,comment
from django.views.generic import ListView,DeleteView,CreateView,DetailView,UpdateView
from .forms import postform,Registration,commentForm,profileupdate
from django.urls import reverse_lazy,reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def likeview(request,pk):
	post = get_object_or_404(Post, id = request.POST.get('post_id'))
	liked = False
	if post.likes.filter(id = request.user.id).exists():
		post.likes.remove(request.user)
		liked = False
	else:
		post.likes.add(request.user)
		liked=True
	return HttpResponseRedirect(reverse('show-one', args = [str(pk)]))


class showpost(ListView):
	model = Post
	template_name = 'show-post.html'
	ordering = ['-created']
	fields = ['__all__']	

 
class addpost(CreateView):
	#model = Post
	form_class = postform
	template_name = 'addpost.html'
	def get_initial(self, *args, **kwargs):
		initial = super(addpost, self).get_initial(**kwargs)
		initial['author'] = self.request.user
		return initial



class detail(DetailView):
	model = Post
	template_name = 'show-one.html'
	def get_context_data(self, *args, **kwargs):
		context = super(detail, self).get_context_data()
		post = get_object_or_404(Post,id = self.kwargs['pk'])
		likes = post.total_likes()

		liked = False
		if post.likes.filter(id = self.request.user.id).exists():
			liked = True
		else:
			liked = False

		context['total_likes'] = likes
		context['liked'] = liked
		return context



class update(UpdateView):
	model= Post
	template_name = 'edit-post.html'
	fields = ['title','detail']


	
class delete(DeleteView):
	model = Post
	template_name = 'delete-post.html'
	success_url = reverse_lazy('show-post')

from django.views import generic
from django.contrib.auth.forms import UserCreationForm

class registration(generic.CreateView):
	#form_class = UserCreationForm
	form_class = Registration
	template_name = 'registration/register.html'
	success_url = reverse_lazy('login')



def user_login(request):
	if request.method == 'POST':
		user= request.POST.get('username')
		passw = request.POST.get('password')
		user = authenticate(request,username=user,password=passw)
		if user is not None:
			login(request, user)
			return redirect('show-post')
		else:
			messages.error(request,'Try Again')
			return render(request,'registration/login.html')

	return render(request,'registration/login.html')

class showprofile(DetailView):
	model = User
	template_name = 'profile.html'
	def get_context_data(self,*args,**kwargs):
		users = User.objects.all()
		context = super(showprofile,self).get_context_data()
		user = get_object_or_404(User,id = self.kwargs['pk'])
		context['user'] = user


class UserEditForm(UpdateView):
	form_class = profileupdate
	template_name= 'registration/edit_profile.html'
	success_url = reverse_lazy('show-post')
	#fields = ['username','email','password']


	def get_object(self):
		return self.request.user

class comment(CreateView):
	#model = Comment
	form_class = commentForm
	template_name  = 'comment.html'

	def form_valid(self,form):
		form.instance.post_id = self.kwargs['pk']
		return super().form_valid(form)


	




 