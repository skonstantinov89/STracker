from django.shortcuts import render_to_response, redirect
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext


# Create your views here.

class Login(View):
    def get(self,request):
        context = RequestContext(request)
        return render_to_response('login.html', context)

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
        return render_to_response('login.html', context)

    def post(self, request):
        context = RequestContext(request)
        logout(request)
        
class Home(LoginRequiredMixin, View):
    """
    This function render the content for the home page of the application after the user is loged in
    """
    def get(self,request):
        context = RequestContext(request)
        return render_to_response('index.html',context)
    def post(self,request):
        raise Http404("Operation is not allowed!")
