from django.shortcuts import render, redirect
from ..login_app.models import User
from models import Video

# Create your views here.

def dashboard(request):
    a = User.objects.get(id = request.session['id'])

    context = {
        'user': User.objects.get(id = request.session['id']),
        'videos': Video.objects.filter(creator__id = a.id)
    }

    return render(request, 'planner_app/dashboard.html', context)


def newVideo(request):
    return render(request,'planner_app/newvideo.html')

def create(request):
    Video.objects.create(video_number=request.POST['video_number'], title= request.POST['title'], playlist=request.POST['playlist'], description=request.POST['description'], preperation=request.POST['preperation'], materials= request.POST['materials'], tags=request.POST['tags'], creator=User.objects.get(id=request.session['id']))
    return redirect("/main/dashboard")

def show(request, id):
    context = {
        'video': Video.objects.get(id=id)
    }

    return render(request, 'planner_app/show_video.html', context)

def delete(request, id):
    Video.objects.get(id=id).delete()
    return redirect("/main/dashboard")

def update(request, id):
    context ={
        'video': Video.objects.get(id=id)
    }
    return render(request, 'planner_app/update.html', context)

def change(request, id):
    video = Video.objects.get(id=id)
    video.video_number = request.POST['video_number']
    video.title = request.POST['title']
    video.playlist = request.POST['playlist']
    video.description = request.POST['description']
    video.preperation = request.POST['preperation']
    video.materials = request.POST['materials']
    video.tags = request.POST['tags']
    video.save()
    return redirect('/main/dashboard')