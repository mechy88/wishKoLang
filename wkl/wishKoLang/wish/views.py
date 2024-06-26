from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
# from rest_framework import status
# from rest_framework.response import Response

from .models import User
from .serializers import UserSerializer

#test
def users(request):
    users = User.objects.all()
    series = UserSerializer(users, many=True)
    return JsonResponse({'drinks':series.data})

# Create your views here.
def index(request):
    return HttpResponse("Hello, World!")

def welcome(request):
    return render(request, "wish/subpages/Initials/welcome.html")

@api_view(['GET', 'POST'])
def login(request):
    if request.method == 'GET':
        return render(request, "wish/subpages/Initials/login.html")
    elif request.method == 'POST':
        try:
            username = request.POST.get("username")
            password = request.POST.get("password")
            account = User.objects.get(username=username) # user found, check to see
        except User.DoesNotExist:
            error_message = 'User does not exist'
            return render(request, "wish/subpages/Initials/login.html", {'error_message': error_message})
        if account.password == password:
            return render(request, "wish/pages/home.html")
        else:
            error_message = 'Incorrect password'
            return render(request, "wish/subpages/Initials/login.html", {'error_message': error_message})

@api_view(['GET', 'POST'])
def signup(request):
    if request.method == 'GET':
        return render(request, "wish/subpages/Initials/signup.html")
    elif request.method == 'POST':
        
        username = request.POST.get("username")
        password = request.POST.get("password")
        confirmPassword = request.POST.get("confirmPassword")            
        if password != confirmPassword:
            error_message = 'Confirm password does not match'
            return render(request, "wish/subpages/Initials/signup.html", {'error_message': error_message})
        if User.objects.filter(username=username).count():
            error_message = 'User already exists'
            return render(request, "wish/subpages/Initials/signup.html", {'error_message': error_message})
        registered = User(username=username, password=password)
        registered.save()

        return render(request, "wish/subpages/Initials/setup.html", {"id":registered.id, "username":registered.username})

@api_view(['GET', 'POST'])
def setup(request):
    if request.method == 'GET':
        return render(request, "wish/subpages/Initials/setup.html")
    if request.method == 'POST':
        id = request.POST.get("id")
        profilePicture = request.POST.get("username")
        birthday = request.POST.get("birthday")
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        emailaddress = request.POST.get("emailaddress")
        bio = request.POST.get("bio")
        try:
            account = User.objects.get(id=id) # user found, check to see
            account.profile_picture_link = profilePicture
            account.birthday = birthday
            account.first_name = firstname
            account.last_name = lastname
            account.email = emailaddress
            account.bio = bio
            account.save()
            print(account)
            return render(request, "wish/pages/home.html")
        except User.DoesNotExist:
            error_message = 'User does not exist'
            return render(request, "wish/subpages/Initials/setup", {'error_message': error_message})

def home(request):
    return render(request, "wish/pages/home.html")

def openGifting(request):
    return render(request, "wish/pages/openGifting.html")

def organization(request):
    return render(request, "wish/subpages/OpenGifting/organization.html")

def secretSanta(request):
    return render(request, "wish/pages/secretSanta.html")

def createGroup(request):
    return render(request, "wish/subpages/SecretSanta/createGroup.html")

def group(request):
    return render(request, "wish/subpages/SecretSanta/group.html")

def runRoulette(request):
    return render(request, "wish/subpages/SecretSanta/runRoulette.html")

def friends(request):
    return render(request, "wish/pages/friends.html")