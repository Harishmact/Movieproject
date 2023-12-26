from django.shortcuts import render
from movie1.models import mnames
from movie1.forms import mforms

# Create your views here.
def home(request):
    b=mnames.objects.all()


    return render(request,"home.html",{'mov':b})
def addmovie(request):
    if (request.method == "POST"):
        img = request.FILES['i']
        n = request.POST['t']
        d = request.POST['d']
        y = request.POST['y']
     #sending values from the userdefined form to dbtable
        b = mnames.objects.create(image=img, name=n, dec=d, year=y)
        b.save()
        return home(request)

    return render(request,"addmovie.html")

def description(request,p):
    b=mnames.objects.get(id=p)
    return render(request,"desc.html",{'mov':b})

def editmovie(request,p):
    b=mnames.objects.get(id=p)
    form=mforms(instance=b)
    #after editing the fields
    if(request.method=="POST"):
        form=mforms(request.POST,request.FILES,instance=b)
        if(form.is_valid()):
            form.save()
            return home(request)

    return render(request,"editmovie.html",{'form':form})

def deletemovie(request,p):
    b=mnames.objects.get(id=p)
    b.delete()
    return home(request)

