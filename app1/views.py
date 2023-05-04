from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
    my_dict={
        "title":"salaaaam",
        "contex":"ssadadsa addasf afsfs"
    }
    return render(request,'page.html',context={"test":my_dict})
