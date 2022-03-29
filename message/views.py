from django.shortcuts import render,redirect
from message.models import Room,Message,Topic
from app.models import Post
from message.form import RoomForm
from django.db.models import Q

# Create your views here.


def room(request,pk):
	name = Post.objects.get(id = pk)
	if Room.objects.filter(Room_name = name.title).exists():
		room = Room.objects.get(Room_name = name.title)
		room_messages  = room.message_set.all()
		participants = room.participants.all()
		if request.method =='POST':
			message = Message.objects.create(

			 user =  request.user,
			 room  =  room,
			 body = request.POST.get('body'),
				)
			room.participants.add(request.user)
			x = room.id
			return redirect('room',pk = name.id)

	else:
		Room.objects.create(host=name.author,Room_name=name.title,description=name.detail,created=name.created)
		room_messages = room.message_set.all()
		participants = room.participants.all()
		if request.method =='POST':
			message = Message.objects.create(
				user = request.user,
				room = room,
				body = request.POST.get(body),
				)
			room.participants.add(request.user)
	context = {'room':room,'room_messages':room_messages
				, 'participants':participants,'post':name}

	return render(request,'room.html',context)


def create_room(request):
	form = RoomForm()

	if request.method == 'POST':
		form = RoomForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('show-post')

	context = {"form": form}
	return render(request,'room_create.html',contex )