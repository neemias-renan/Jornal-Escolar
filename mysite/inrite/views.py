
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import View

from .models import Comment, Edition, News


class IndexView(View):
    def get(self, request):
        edition = Edition.objects.first()
        all_editions = Edition.objects.all()
        all_news = News.objects.filter(edition = edition).order_by('-date')

        first_new = News.objects.last()

        context = {
            "edition":edition,
            "first_new": first_new,
            "all_editions":all_editions,
            "all_news":all_news,
        }
        return render(request, 'inrite/index.html', context)
    
    def post(self, request):
        edition_selected = request.POST.get("select")
        edition = Edition.objects.filter(title = edition_selected).first()
        all_editions = Edition.objects.all()
        all_news = News.objects.filter(edition = edition).order_by('-date')

        first_new = News.objects.last()

        context = {
            "edition":edition,
            "first_new": first_new,
            "all_editions":all_editions,
            "all_news":all_news,
        }
        return render(request, 'inrite/index.html', context)


class SearchView(View):
    def get(self, request):
        edition = Edition.objects.first()
        all_editions = Edition.objects.all().order_by('date')
        all_news = News.objects.filter(edition = edition).order_by('-date')

        first_new = News.objects.last()

        context = {
            "first_new": first_new,
            "all_editions":all_editions,
            "all_news":all_news,
        }
        return render(request, 'inrite/search.html', context)
    
    def post(self, request):
        input_search = request.POST.get("search")
        all_editions = Edition.objects.all().order_by('date')
        all_news = News.objects.filter(title__contains=input_search).order_by('-date')
        first_new = News.objects.last()


        context = {
            "input_search":input_search,
            "first_new": first_new,
            "all_editions":all_editions,
            "all_news":all_news,
        }
        return render(request, 'inrite/search.html', context)
    

class NewsView(View):
    def get(self, request, *args, **kwargs):
        new = get_object_or_404(News, pk=kwargs['pk'])
        all_comments = Comment.objects.filter(news = new)

        context = {
            "new": new,
            "all_comments": all_comments,
        }
        return render(request, 'inrite/new.html', context)
    
    def post(self, request, *args, **kwargs):
        new = get_object_or_404(News, pk=kwargs['pk'])
        comment = request.POST.get("comment")
        author = request.user

        Comment.objects.create(body=comment,news = new, author = author)
        return HttpResponseRedirect(reverse('inrite:new', kwargs={'pk': kwargs['pk']}))
    
class ManagerView(View):
    def get(self, request, *args, **kwargs):
        all_editions = Edition.objects.all()
        context = {
            "all_editions":all_editions,
        }
        return render(request, 'inrite/manager.html', context)
    
    def post(self, request, *args, **kwargs):
        edition_selected = request.POST.get("edition_select")
        if(edition_selected == "new_edition"):
            new_edition = request.POST.get("edition_new")
            edition = Edition.objects.create(title = new_edition)
        else:
            edition = Edition.objects.filter(title = edition_selected).first()
     
        new_title= request.POST.get("news_title")
        new_description= request.POST.get("news_description")
        new_content= request.POST.get("news_content")
        author = request.user

        News.objects.create(title = new_title, body = new_content, description=new_description, edition = edition, author = author.profile)
        return HttpResponseRedirect(reverse('inrite:index'))

class LoginView(View):
    def get(self, request, *args, **kwargs):
        
        context = {}
        return render(request, 'inrite/login.html', context)
    
    def post(self, request, *args, **kwargs):
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('inrite:index'))
        else:
            context = {
                "message": "Usuário ou senha incorretos!",
            }            
            return render(request, 'inrite/login.html', context)

class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(reverse('inrite:index'))

class SignupView(View):
    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, 'inrite/signup.html', context)

    def post(self, request, *args, **kwargs):
        return HttpResponseRedirect(reverse('inrite:index'))
