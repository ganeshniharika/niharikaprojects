from django.shortcuts import render
from .models import regddata
from .forms import regd_form

def regd_view(request):
    if request.method=='POST':
        rform=regd_form(request.POST or None)
        if rform.is_valid():
            user=rform.cleaned_data.get("username")
            mail=rform.cleaned_data.get("email")
            mob=rform.cleaned_data.get("mobile")

            data=regddata(
                username=user,
                email=mail,
                mobile=mob
            )
            data.save()
            rform=regd_form()
        return render(request,"valid.html",{'rform':rform})
    else:
        rform = regd_form()
        return render(request, "valid.html", {'rform': rform})

