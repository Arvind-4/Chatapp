from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

from .models import Chat, ChatRoom
from .forms import JoinForm

# Create your views here.

User = get_user_model()


@login_required()
def home(request):
    info = User.objects.get(username=request.user.username)
    form = JoinForm(request.POST or None)
    if form.is_valid():
        room_name = form.cleaned_data.get('name')
        qs = ChatRoom.objects.filter(name=room_name)
        if qs:
            qs_user = ChatRoom.objects.get(name__iexact=room_name)
            room = qs_user.name
            op = qs_user.user.add(info)
            print('The op is ', op)
        else:
            room = ChatRoom.objects.create(
                name=room_name,
            )
            room.user.add(info)
        redirect_url = f'/chat/{room}/'
        return redirect(redirect_url)
    context = {
        'form': form,
    }
    return render(request, 'chat/enter_room.html', context=context)


@login_required()
def room(request, room_name):
    info = User.objects.get(username=request.user.username)
    qs_room_check = ChatRoom.objects.filter(name=room_name)
    if not qs_room_check:
        return redirect('/error/')
    qs_user = ChatRoom.objects.get(name__iexact=room_name)
    if not qs_user:
        return redirect('/error/')
    qs_user.user.add(info)
    qs_user = User.objects.get(username=request.user.username)
    if not qs_user:
        username = ''
    else:
        username = qs_user.username
    obj = Chat.objects.filter(room__name=room_name)
    if obj.exists():
        qs = obj
    else:
        qs = ''
    qs_chat = ChatRoom.objects.filter(user=request.user)
    user_json = username
    context = {
        'username': user_json,
        'req_username': request.user.username,
        'room_name': room_name,
        'messages': qs,
        'room_list': qs_chat,
    }
    return render(request, 'chat/room.html', context=context)


@login_required()
def room_list_view(request):
    qs = ChatRoom.objects.filter(user=request.user)
    if not qs.exists():
        room_list = ''
    else:
        room_list = qs
    context = {
        'room_list': room_list,
    }
    return render(request, 'chat/room_list.html', context=context)
