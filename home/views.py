from django.shortcuts import render
from .models import *

# Create your views here.
def login(request):
    return render(request, 'login.html')

def logout(request):
    return render(request, 'logout.html')

def signup(request):
    return render(request, 'signup.html')

def index(request):
    return render(request, 'index.html')

def home(request):
    images = AboutImage.objects.all()
    cards = ServiceCard.objects.all()
    projects = ProjectCard.objects.all()
    webdevprojects=WebDevProjectCard.objects.all()
    appdevprojects = AppDevProjectCard.objects.all()
    pythondevprojects=PythonDevProjectCard.objects.all()
    uiuxprojects = UIUXProjectCard.objects.all()
    achivementcardmodels= AchivementCardModel.objects.all()
    achivementcards = AchivementCard.objects.all()
    certificates = certificate.objects.all()
    # Assuming 'blog' is a model you want to include
    blogs = blog.objects.all()
    return render(request, 'home.html', {'images': images,'cards': cards,'projects':projects,'webdevprojects':webdevprojects,'appdevprojects':appdevprojects,'pythondevprojects':pythondevprojects,'uiuxprojects':uiuxprojects,'achivementcardmodels':achivementcardmodels,'achivementcards':achivementcards,'certificates':certificates,'blogs': blogs})

def codesence(request):
    return render(request, 'codesence.html')

def shop(request):
    return render(request, 'home.html')







#Additional Pages of road maps
def front(request):
    return render(request, 'front.html')
def back(request):
    return render(request, 'back.html')
def software(request):
    return render(request, 'software.html')
def database(request):
    return render(request, 'database.html')