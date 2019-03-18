from django.shortcuts import render
from .models import Productdata
from .forms import insertingdataform,updatingdataform,deletingdataform
from django.http.response import HttpResponse

# Create your views here.
def home(request):
    return render(request,'home.html')

def insertingdataview(request):
    if request.method =='POST':
        iform = insertingdataform(request.POST)
        if iform.is_valid():
            pno=request.POST.get('product_number','')
            pname=request.POST.get('product_name','')
            pcost=request.POST.get('product_cost','')
            pclass=request.POST.get('product_class','')
            pweight=request.POST.get('product_weight','')
            data=Productdata(
                product_number=pno,
                product_name=pname,
                product_cost=pcost,
                product_class=pclass,
                product_weight=pweight,
            )
            data.save()
            iform = insertingdataform()
            return render(request,'insertingdata.html',{'iform': iform})
    else:
        iform=insertingdataform()
        return render(request,'insertingdata.html',{'iform':iform})


def updatingdataview(request):
    if request.method=='POST':
        uform = updatingdataform(request.POST)
        if uform.is_valid():
            pno = request.POST.get('product_number', '')
            pcost = request.POST.get('product_cost', '')
            pdata=Productdata.objects.filter(product_number=pno)
            if not pdata:
                return HttpResponse("no id available")
            else:
                pdata.update(product_cost=pcost)
                uform = updatingdataform()
                return render(request, 'update.html', {'uform': uform})

    else:
        uform=updatingdataform()
        return render(request,'update.html',{'uform':uform})


def deletingdataview(request):
    if request.method == 'POST':
        uform = deletingdataform(request.POST)
        if uform.is_valid():
            pno = request.POST.get('product_number', '')
            data=Productdata.objects.filter(product_number=pno)
            if data:
                data.delete()

            else:
                return HttpResponse("id not available")
            dform = deletingdataform()
            return render(request, 'delete.html', {'dform': dform})

    else:
        dform = deletingdataform()
        return render(request, 'delete.html', {'dform': dform})


def accessdataview(request):
    data = Productdata.objects.all()
    return render(request,'access.html',{'data':data})