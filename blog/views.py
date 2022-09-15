from django.shortcuts import render
import datetime
from .models import *
from django.shortcuts import render
from django.db import IntegrityError
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth import authenticate
from django.contrib.auth.models import User, auth

def Home(request):
    if request.user.is_authenticated:
        return redirect('/Bloghome')
    return render(request, 'Landingpage.html')

def Signup(request):
    if request.method == 'POST':
        if request.POST['Password'] == request.POST['Confirmpassword']:
            try:
                User.objects.create_user(username=request.POST['Username'], email=request.POST['Emai'], password=request.POST['Password'])
                user = authenticate(username=request.POST['Username'], password=request.POST['Password'])
                if user is not None:
                    auth.login(request, user)
                    return redirect('/')
            except IntegrityError as e:
                return render(request, 'Signup.html', {'message':'Username taken choose another one' })
        else:
            return render(request, 'Signup.html', {'message':'Your passwords did not match😔' })
    return render(request, 'Signup.html')

def Login(request):
    if request.method=='POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            return render(request, 'Landingpage.html', {'message':'Invalid Credentials😔'})
    return redirect('/')

def Logout(request):
    auth.logout(request)
    return redirect('/')

def Bloghome(request):
    if request.user.is_authenticated:
        for i in User.objects.all():
            return render(request, 'Home.html',{
            'Articles':Article.objects.order_by("-date"),
            'Allarticles':Article.objects.all(), 
            'Myarticles':Article.objects.filter(user=request.user).order_by("-date"),
            'Authors':User.objects.all(),
            'Time':int(datetime.now().strftime("%H")),
             })
    else:
        return redirect('/')

def Myarticles(request):
    return render(request, 'Yourarticles.html', {'Article':Article.objects.filter(user=request.user).order_by("-date")})

def Profile(request):
    if request.user.is_authenticated:
        return render(request, 'Profile.html', {'User':request.user})
    else:
        return redirect('/')

def Updateprofile(request):
    if request.method == "POST":
        lusername = request.user.username
        if(request.FILES.get('Pic')==None and request.POST['Email']=="" and request.POST['Username']=="" and request.POST['Password']==""):
            messages.error(request, "Nothing has been changed")
        else:
            if(request.FILES.get('Pic')):
                request.user.profile.pic=request.FILES.get('Pic')
                request.user.save()
                messages.error(request, 'Profile updated successfully')
            if (request.POST['Email']):
                request.user.email = request.POST['Email']
                request.user.save()
                messages.error(request, 'Profile updated successfully')
            if(request.POST['Username']):
                try:
                    request.user.username = request.POST['Username']
                    request.user.save()
                    messages.error(request, 'Profile updated successfully')
                except IntegrityError as e:
                    messages.error(request, "Username already taken")
            if (request.POST['Password']):
                request.user.password = request.POST['Password']
                request.user.save()
        return redirect('/Profile')
    return redirect('/Profile')

def Createpost(request):
    if request.method=="POST":
        Article_save = Article(user=request.user, title=request.POST.get('Posttitle'), desc= request.POST.get('Postdes'),pic=request.FILES.get('Pic'))
        Article_save.save()    
        return redirect('/')
    return redirect('/')


def Updatepost(request, Author_id):
    if (request.method=="POST"):
        lpic=Article.objects.get(id=Author_id).pic
        Article.objects.filter(id=Author_id).update(title=request.POST['Posttitle'], desc=request.POST['Postdes'])
        if(request.FILES.get('Pic')):
            Article.objects.filter(id=Author_id).update(pic=request.FILES.get('Pic'))
        return redirect('/Myarticles')
    article=Article.objects.filter(id=Author_id).values()
    return render(request, 'Updatearticle.html', {'articledata':article})

def Removeprofilepic(request):
    request.user.profile.pic="Defaultprofilepic.jpg"
    request.user.save()
    messages.error(request, 'Profile picture removed')
    return redirect('/Profile')
def Delete(request, Article_id):
    Article.objects.filter(id=Article_id).delete()
    return redirect('/Myarticles')

def Deleteall(request):
    articles = Article.objects.filter(user = request.user.id)
    for i in articles:
        Article.objects.get(id=i.id).delete()
    return redirect('/Myarticles')

def detail(request, Article_id):
    return render(request, 'Detail.html', {'Article':Article.objects.get(id=Article_id)})
def Search(request):
    if(request.method=="POST"):
        searchquery = request.POST['search']
        if(Article.objects.all().filter(title__icontains=searchquery)):
            return render(request, 'Home.html',{'Articles':Article.objects.all().filter(title__icontains=searchquery),'Allarticles':Article.objects.all(), 'Myarticles':Article.objects.filter(user=request.user).order_by("-date"), 'Authors':User.objects.all(), 'Message':'Articles with the keyword '+'"'+searchquery+'"'+' in their title','Click':'| Clear Search'})
        return render(request, 'Home.html',{'Articles':Article.objects.filter(user__username=searchquery),'Allarticles':Article.objects.all(), 'Myarticles':Article.objects.filter(user=request.user).order_by("-date"), 'Authors':User.objects.all(), 'Message':'There are no articles having title '+'"'+searchquery+'"','Click':'| Clear Search'})
    return redirect('/')

def Sort(request):
    return render(request, 'Home.html',{'Articles':Article.objects.order_by("date"),'Allarticles':Article.objects.all(), 'Myarticles':Article.objects.filter(user=request.user).order_by("-date"), 'Authors':User.objects.all(), 'Message':'Articles sorted in ascending order of "publication date" |','Click':'Remove sort'})
def Sortmine(request):
    return render(request, 'Yourarticles.html', {'Article':Article.objects.filter(user=request.user).order_by("date"),'Message':'Articles sorted in ascending order of "publication date" |','Click':'Remove sort'})
def Authorpage(request, Article_id):
    Articleauthor=User.objects.get(id=Article_id).id
    if(request.user.id == Articleauthor):
        return render(request, 'Yourarticles.html', {'Article':Article.objects.filter(user=request.user)})
    return render(request, 'Authorpage.html', {"Article":[Article.objects.filter(user=Articleauthor), User.objects.get(id=Article_id)]})