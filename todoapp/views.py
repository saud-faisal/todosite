from django.shortcuts import render
from todoapp.models import TodoApp
from django.http import HttpResponse

# Create your views here.
def call(request):
    return render(request,'index.html')

def add(request):
    if request.method=='POST':
        obj=TodoApp()
        obj.description=request.POST.get('description')
        obj.type=request.POST.get('type')
        obj.save()
        rec=TodoApp.objects.all()
        return render(request,'index.html',{'rec':rec})
    return HttpResponse("error in add")
def delete(request):
    if request.method=='POST':
        id=request.POST.get('id')
        # b=TodoApp.objects.filter(id=id1)
        # b.delete()
        # return render(request,'index.html')
        TodoApp.objects.filter(id=id).delete()
        return render(request,'index.html')
    else:
        return HttpResponse("errors")
    return HttpResponse("errrs in delete")
