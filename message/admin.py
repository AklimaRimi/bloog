from django.contrib import admin
from message.models import Topic, Room,Message

# Register your models here.

admin.site.register(Topic)
admin.site.register(Room)
admin.site.register(Message)


