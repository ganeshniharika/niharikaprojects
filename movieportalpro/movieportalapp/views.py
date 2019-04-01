from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Telugu,English,Hindi,Bookdata


def home(request):
    return render(request,'home.html')


def output(request):
    req=request.GET['movie']
    if req=='telugu':
        return redirect(telugu)
    elif req=='english':
        return redirect(english)
    elif req=='hindi':
        return redirect(hindi)
def telugu(request):
    tm=Telugu.objects.all()
    return render(request,'telugu.html',{'tm':tm})
def english(request):
    em=English.objects.all()
    return render(request,'english.html',{'em':em})
def hindi(request):
    hm=Hindi.objects.all()
    return render(request,'hindi.html',{'hm':hm})

def book(request):
    if request.method=="POST":
        id=request.POST.get('id','')
        data=Telugu.objects.filter(id=id)
        return render(request,'book.html',{'data':data})


def conform(request):
    if request.method=="POST":
        id=request.POST.get('id',' ')
        m_name=request.POST.get('mname',' ')
        m_time=request.POST.get('time',' ')
        t_name=request.POST.get('theatre',' ')
        c_class=request.POST.get('class',' ')
        #t_name=request.POST.get('theatre',' ')
        data=Bookdata(
            m_id=id,
            m_name=m_name,
            m_time=m_time,
            m_theatre=t_name,
            c_class=c_class
        )
        data.save()

        return HttpResponse("ticket conformed...")