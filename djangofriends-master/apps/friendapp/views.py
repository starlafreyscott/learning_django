from django.shortcuts import render
from . import models
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.

#
# def index(req):
#     users = models.Users.objects.all()
#     context = {'users': users}
#     return render(req, "friendapp/index.html", context)


def index(req):
    users = ''  # TODO set default to stop error
    # users = models.Users.objects.all()  # TODO This was broken
    # users = models.Users.objects.filter(last_name='Rodriguez')
    # users = models.Users.objects.exclude(last_name='Rodriguez')
    # users = models.Users.objects.filter(last_name='Rodriguez') | models.Users.objects.filter(first_name='Daniel')
    # users = models.Users.objects.filter(last_name='Rodriguez') | models.Users.objects.exclude(first_name='Madison')
    # users = models.Users.objects.filter(last_name='Rodriguez').exclude(first_name='Madison')
    # users = models.Users.objects.all().exclude(first_name='Daniel').exclude(first_name='Michael').exclude(last_name='Rodriguez')
    # users = models.Users.objects.get(id=4)
    # users = models.Users.objects.get(last_name='Rodriguez')  # This does not work! It will return all objects with this last name
    # users = models.Users.objects.get(id=10000)  # this returns an error because no id 10000
    # users = models.Users.objects.order_by('first_name')
    # users = models.Users.objects.order_by('-last_name')
    # users = models.Friendships.objects.all()
    # user_id = models.Friendships.objects.get(id=4)
    # users = models.Users.objects.filter(id=user_id.friend_id)

    # a_list = []
    # for friend in users:
    #     temp = models.Users.objects.get(id=friend.friend_id)  # THIS IS FUCKING NUTS WTF
    #     a_list.append(temp)
    # users = models.Friendships.objects.all().exclude(user_id=(4, 5, 6)).order_by('created_at')
    # a_list = [] # HEY THIS GIVES DOUBLES OF SOME PEOPLE NOT SURE HOW TO FIX!
    # for friend in users:
    #     temp = models.Users.objects.get(id=friend.friend_id)
    #     a_list.append(temp)
    # users = models.Users.objects.filter(id=users)
    # users = models.Friendships.objects.filter(user__id=2)
    # users = models.Friendships.objects.values('user_id', 'friend_id')
    # for friends in users:
    #     print friends.friend_id
    # users = models.Friendships.objects.filter(user__first_name='Michael')
    # # users = ''
    # user_list = []
    # for friends in users:
    #     temp = models.Users.objects.filter(id=friends.friend_id).values('first_name', 'last_name')
    #     temp = temp[0]
    #     user_list.append(temp)
    #     print friends.friend_id
    # users = models.Users.objects.filter(id='1')
    # users = models.Users.objects.filter(usersfriend__friend__last_name="Hernandez").distinct()
    # users = models.Users.objects.raw('SELECT * FROM friendships')
    # Add this line!
    try:
        users = models.Users.objects.get(id=1)
        print("this worked")
    except ObjectDoesNotExist:
        print("no user")
    # users = models.Users.objects.filter(usersfriend__friend__id=2)
    # users = models.Friendships.objects.select_related('friend').filter(user_id=2)  # num 3 part two
    # print (users.query)
    # print (users)
    # print user_list

    # print (users)  # TODO find a better way to handle this
    # end of add
    context = {'users': users}
    return render(req, "friendapp/index.html", context)
