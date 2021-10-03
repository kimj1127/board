from django.shortcuts import redirect, render
from .models import Topic, Choice
# Create your views here.
def index(request):
    t = Topic.objects.all()
    context = {
        'con' : t,
    }
    return render(request, "vote/index.html", context)

def create(request):
    if request.method == "POST":
        title = request.POST.get("title")
        writer = request.user.username
        writer_pic = request.user.pic
        comment = request.POST.get("comment")
        if title:
            t = Topic(title=title, writer=writer, writer_pic=writer_pic, comment=comment)
            subject = request.POST.getlist("subject")
            pic = request.FILES.getlist("pic")
            t.save()
            for i,j in zip(subject, pic):
                Choice(title=t, subject=i, pic=j).save()

        return redirect("vote:index")

    return render(request, 'vote/create.html')

def detail(request, num):
    t = Topic.objects.get(id=num)
    c = t.choice_set.all()
    context = {
        'con' : t,
        'cho' : c,
    }
    return render(request, 'vote/detail.html', context)

def vote(request, conid):
    t = Topic.objects.get(id=conid)
    if not request.user in t.voter.all():
        t.voter.add(request.user)
        s = request.POST.get('subject')
        c = Choice.objects.get(id=s)
        c.choicer.add(request.user)

    return redirect("vote:detail", num=conid)