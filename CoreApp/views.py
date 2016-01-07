from django.shortcuts import render_to_response, redirect
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext
from CoreApp.models import Tickets, Projects
from django.db.models import Q
from django.http import Http404
from django.db import IntegrityError



# Create your views here.

class Login(View):
    def get(self,request):
        context = RequestContext(request)
        return render_to_response('core/login.html', context)

    def post(self, request):
        context = RequestContext(request)
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('/home', context)
        else:
            return redirect('/logout', context)
class Logout(View):
    def get(self,request):
        context = RequestContext(request)
        logout(request)
        return redirect('/home', context)

    def post(self, request):
        context = RequestContext(request)
        logout(request)

class Home(LoginRequiredMixin, View):
    """
    This function render the content for the home page of the application after the user is loged in
    """
    def get(self,request):
        context = RequestContext(request)
        taskData = Tickets.objects.filter(~Q(status='finished'))
        user = {
            'name': request.user.first_name,
            'sirname': request.user.last_name,
            'username': request.user.username,
            'email': request.user.email
        }
        return render_to_response('core/dashboard.html', locals(), context)
    def post(self,request):
        context = RequestContext(request)
        raise Http404("Operation is not allowed!")

class addTasks(LoginRequiredMixin, View):
    def get(self,request):
        context = RequestContext(request)
        projects = Projects.objects.all()
        return render_to_response('new-tasks/add-task.html', locals(), context)

    def post(self,request):
        context = RequestContext(request)
        header = request.POST.get('header')
        priority = request.POST.get('priority')
        comment = request.POST.get('comment')
        project = request.POST.get('project')
        projectObject = Projects.objects.get(id = int(project))
        # try:
        newTicket = Tickets.objects.create(
        header = header,
        priority = priority,
        comment = comment,
        createUserID = request.user,
        projectID = projectObject
    )
        # except IntegrityError:
        #     message = 'Неправилно попълнени или пропуснати данни!'
        #     return render_to_response('new-tasks/failure.html', locals(), context)
        message = u"Успешно добавяне на нова заявка!"
        return render_to_response('new-tasks/success.html', locals(), context)

class addProject(LoginRequiredMixin, View):
    def get(self,request):
        context = RequestContext(request)
        return render_to_response('new-tasks/add-project.html', locals(), context)

    def post(self,request):
        name = request.POST.get('name')
        newProject = Projects.objects.create(
            name = name,
        )
        message = u'Успешно създаване на проект!'
        return render_to_response('new-tasks/success.html', locals(), context)
