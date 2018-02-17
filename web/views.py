# -*- coding: UTF-8 -*-
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.shortcuts import render
from models import Content
from forms import ContentForm, LoginForm, ContentEditForm
from django.contrib.auth import authenticate, login
from django.utils import timezone
from uuid import uuid4
from django.core.files.storage import FileSystemStorage

def index(request):
        contents = Content.objects.all().order_by("-id")
        return render_to_response('index.html', {'contents': contents}, context_instance=RequestContext(request))


def add(request):
        if request.method == 'POST':
            form = ContentForm(request.POST)
            if form.is_valid():
                obj = form.save(commit=False)
                if "picture" in request.FILES:
                    myfile = request.FILES['picture']
                    fs = FileSystemStorage()
                    filename = uuid4().hex
                    fs.save("static/upload/"+filename, myfile)
                    obj.picname = filename                    
                    obj.save()
                return redirect("/")
        else:
                form = ContentForm()
        return render_to_response('form.html',{'form': form}, context_instance=RequestContext(request))

# 使用者登入功能
def user_login(request):
        message = ""
        if request.method == "POST":
                form = LoginForm(request.POST)
                if form.is_valid():
                        username = request.POST['username']
                        password = request.POST['password']
                        user = authenticate(username=username, password=password)
                        if user is not None:
                            # 登入成功，導到大廳
                            login(request, user)
                            return redirect('/')
                        else:             
                            message = "無效的帳號或密碼!"
        else:
                form = LoginForm()
        return render_to_response('login.html', {'message': message, 'form': form}, context_instance=RequestContext(request))

def edit(request, content_id):
        content = Content.objects.get(id=content_id)
        if request.method == 'POST':               
                form = ContentEditForm(request.POST or None, instance=content)        
                if form.is_valid():
                        form.save()
                        content.handle_date = timezone.now()
                        content.save()                
                        return redirect("/")
        else:
                form = ContentEditForm(instance=content)
        return render_to_response('form_edit.html',{'form': form, 'content':content}, context_instance=RequestContext(request))
      
