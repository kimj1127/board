from django.shortcuts import redirect, render
from .models import Board
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    kw = request.GET.get("kw", '')
    cate = request.GET.get("cate", '')
    if kw:
        
        if cate == "subject":
            b = Board.objects.filter(subject__startswith=kw)
        elif cate == "writer":
            b = Board.objects.filter(writer=kw)
        else:
            b = Board.objects.filter(content__contains=kw)
    else:
        b = Board.objects.all()

    page = request.GET.get("page", 1)


    pag = Paginator(b,10)
    obj = pag.get_page(page)

    context = {
        'con' : obj,
        'kw' : kw,
        'cate' : cate,
    }
    return render(request, "board/index.html", context)

def create(request):
    if request.method == "POST":
        s = request.POST.get('subject')
        w = request.user.username
        c = request.POST.get('content')
        if s and c:
            Board(subject=s, writer=w, content=c).save()
        return redirect("board:index")
    return render(request, "board/create.html")

def detail(request, num):
    b = Board.objects.get(id=num)
    context = {
        'con' : b,
    }
    return render(request, "board/detail.html", context)
def vote(request, conid):
    b = Board.objects.get(id=conid)
    b.up.add(request.user)
    return redirect('board:detail', num=conid)
def cancel(request, conid):
    b = Board.objects.get(id=conid)
    b.up.remove(request.user)
    return redirect('board:detail', num=conid)