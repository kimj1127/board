from django.db.models.query_utils import RegisterLookupMixin
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from .models import User
# Create your views here.
def index(request):
    return render(request, "base.html")

def login_user(request):
    if request.method == "POST":
        u = request.POST.get('username')
        p = request.POST.get('password')
        user = authenticate(username=u, password=p)

        if user:
            login(request, user)
            return redirect("acc:index")
    return render(request, "acc/login.html")

def signup(request):
    if request.method == "POST": 
        u = request.POST.get('username')
        p = request.POST.get('password')
        c = request.POST.get('comment')
        a = request.POST.get('age')
        pic = request.FILES.get('userimage')  #사진은 POST X FILES O
        if not pic:
            pic = "none.png"
        try:
            User.objects.create_user(username=u, password=p, comment=c, age=a, pic=pic).save() #!!! 암호화 처리로!!!
        except:
            e = {
                'err' : "회원가입실패"
            }
            return render(request, "error.html", context=e)
        return redirect("acc:login")
    return render(request, "acc/signup.html")

def logout_user(request):
    logout(request)
    return redirect("acc:index")

def profile(request):
    return render(request, "acc/profile.html")

def modify(request):
    if request.method == "POST":
        name = request.user.username
        u = User.objects.get(username=name)
        u.age = request.POST.get('age')
        u.comment = request.POST.get('comment')
        p = request.POST.get('password')  # 암호화해서 password 바꿔준다
        u.set_password(p)
        r = request.POST.get('userimage')
        if r:
            u.pic = r
        u.save()
        user = authenticate(username=name, password=p)
        login(request,user)
        return redirect("acc:profile")
    return render(request, "acc/modify.html")